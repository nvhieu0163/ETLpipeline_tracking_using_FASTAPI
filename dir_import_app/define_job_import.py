import timeit
from datetime import datetime

from dir_import_app.import_data import *


def Northwind_orders_SyncJob():
    try:
        start_time = datetime.now().strftime("%H:%M:%S - %d %B %Y")
        # Thực hiện import
        import_Northwind_orders()
    except Exception as ex:
        print("GET ERROR WHEN IMPORT northwind/orders: ", ex)
        raise ex
    finally:
        end_time = datetime.now().strftime("%H:%M:%S - %d %B %Y")
        with open("./dir_import_app/log_import/Northwind/orders.txt", "a") as f:
            f.write(f"Call notify import data at: {start_time}\n")
            f.write(f"Finish import data at: {end_time}\n")


def Northwind_us_states_SyncJob():
    try:
        start_time = datetime.now().strftime("%H:%M:%S - %d %B %Y")
        # Thực hiện import
        import_Northwind_us_states()
    except Exception as ex:
        print("GET ERROR WHEN IMPORT northwind/us_states: ", ex)
        raise ex
    finally:
        end_time = datetime.now().strftime("%H:%M:%S - %d %B %Y")
        with open("./dir_import_app/log_import/Northwind/us_states.txt", "a") as f:
            f.write(f"Call notify import data at: {start_time}\n")
            f.write(f"Finish import data at: {end_time}\n")


# list defined jobs
LIST_JOB = {
    "Northwind_orders_SyncJob" : Northwind_orders_SyncJob,
    "Northwind_us_states_SyncJob" : Northwind_us_states_SyncJob
} 