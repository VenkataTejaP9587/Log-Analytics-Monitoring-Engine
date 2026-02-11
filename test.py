from dask.distributed import Client


def start():
    client = Client()
    print("Dashboard:", client.dashboard_link)
    input("Press Enter to exit...")


if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    start()
