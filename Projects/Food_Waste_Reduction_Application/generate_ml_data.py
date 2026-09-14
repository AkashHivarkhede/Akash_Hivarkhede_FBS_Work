from datetime import date, timedelta
import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from waste_management.models import (
    FoodItem,
    ProductionRecord,
    WasteRecord,
)


class Command(BaseCommand):

    help = "Generate historical production data for ML training"


    def handle(self, *args, **kwargs):

        foods = list(
            FoodItem.objects.filter(
                is_available=True
            )
        )

        if not foods:

            self.stdout.write(
                self.style.ERROR(
                    "No food items found. Add food items first."
                )
            )

            return


        user = (
            User.objects
            .filter(is_active=True)
            .first()
        )


        if not user:

            self.stdout.write(
                self.style.ERROR(
                    "No active user found."
                )
            )

            return


        # -----------------------------------------
        # DATE RANGE
        # -----------------------------------------

        end_date = date.today()

        start_date = (
            end_date
            - timedelta(days=300)
        )


        # -----------------------------------------
        # GENERATE DATA
        # -----------------------------------------

        created_count = 0


        current_date = start_date


        while current_date <= end_date:

            for food in foods:

                # ---------------------------------
                # BASE DEMAND
                # ---------------------------------

                base_demand = random.randint(
                    40,
                    120
                )


                # ---------------------------------
                # WEEKEND EFFECT
                # ---------------------------------

                if current_date.weekday() >= 5:

                    base_demand = int(
                        base_demand * 1.15
                    )


                # ---------------------------------
                # RANDOM DAILY VARIATION
                # ---------------------------------

                sold_quantity = max(
                    1,
                    int(
                        random.gauss(
                            base_demand,
                            10
                        )
                    )
                )


                # ---------------------------------
                # PREPARED QUANTITY
                # ---------------------------------

                extra = random.randint(
                    5,
                    15
                )

                prepared_quantity = (
                    sold_quantity
                    + extra
                )


                # ---------------------------------
                # REMAINING FOOD
                # ---------------------------------

                remaining_quantity = random.randint(
                    0,
                    min(
                        10,
                        prepared_quantity - sold_quantity
                    )
                )


                # ---------------------------------
                # WASTE
                # ---------------------------------

                wasted_quantity = (
                    prepared_quantity
                    - sold_quantity
                    - remaining_quantity
                )


                # ---------------------------------
                # PRODUCTION RECORD
                # ---------------------------------

                record = ProductionRecord.objects.create(

                    food=food,

                    record_date=current_date,

                    prepared_quantity=prepared_quantity,

                    sold_quantity=sold_quantity,

                    remaining_quantity=remaining_quantity,

                    wasted_quantity=wasted_quantity,

                    recorded_by=user

                )


                # ---------------------------------
                # WASTE RECORD
                # ---------------------------------

                if wasted_quantity > 0:

                    waste_reasons = [
                        "Overproduction",
                        "Spoilage",
                        "Damaged",
                        "Expired",
                        "Other",
                    ]

                    reason = random.choice(
                        waste_reasons
                    )


                    waste_cost = (
                        wasted_quantity
                        * food.cost_per_unit
                    )


                    WasteRecord.objects.create(

                        production_record=record,

                        wasted_quantity=wasted_quantity,

                        waste_cost=waste_cost,

                        reason=reason

                    )


                created_count += 1


            current_date += timedelta(
                days=1
            )


        self.stdout.write(

            self.style.SUCCESS(

                f"Successfully created "
                f"{created_count} production records."

            )

        )