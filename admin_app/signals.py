'admin_app/signals.py'
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Avg, Sum
from .models import requesttable, product, MarketTrend, Category

@receiver(post_save, sender=requesttable)
def update_market_trend(sender, instance, **kwargs):
    """
    Signal to update market trend whenever a new request is made.
    """
    today = now().date()
    start_of_this_week = today - timedelta(days=today.weekday())
    start_of_last_week = start_of_this_week - timedelta(days=7)

    categories = product.objects.values('category').distinct()

    for category in categories:
        category_id = category['category']
        category_obj = Category.objects.get(id=category_id)

        # Calculate average prices
        last_week_price = (
            product.objects.filter(category_id=category_id, date__range=[start_of_last_week, start_of_this_week])
            .aggregate(avg_price=Avg('price'))
            .get('avg_price') or 0
        )
        this_week_price = (
            product.objects.filter(category_id=category_id, date__gte=start_of_this_week)
            .aggregate(avg_price=Avg('price'))
            .get('avg_price') or 0
        )

        # Calculate total demand
        total_demand = (
            requesttable.objects.filter(product__category_id=category_id)
            .aggregate(total_quantity=Sum('quantity'))
            .get('total_quantity') or 0
        )

        # Update or create the market trend record
        MarketTrend.objects.update_or_create(
            category=category_obj,
            defaults={
                "last_week_price": last_week_price,
                "this_week_price": this_week_price,
                "demand": total_demand,
            }
        )
