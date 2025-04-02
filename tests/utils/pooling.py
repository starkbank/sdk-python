import time

def wait_for_query(query_func, max_wait_time=10, wait_interval=0.5, *args, **kwargs):
    """
    Waits until the query function (query_func) returns a valid result or until the maximum wait time is reached.
    
    :param query_func: The query function to be executed (e.g., starkbank.merchantinstallment.query)
    :param max_wait_time: Maximum time to wait in seconds (default is 10 seconds)
    :param wait_interval: Time interval between query attempts in seconds (default is 0.5 seconds)
    :param args: Positional arguments to be passed to the query function
    :param kwargs: Keyword arguments to be passed to the query function
    :return: The result of the query function if successful within the maximum wait time
    :raises TimeoutError: If the maximum wait time is exceeded without a valid result
    """
    start_time = time.time()
    
    while True:
        result = query_func(*args, **kwargs)
        
        result_list = list(result)
        
        if result_list:
            return result_list
        
        if time.time() - start_time > max_wait_time:
            raise TimeoutError("Query did not return a result within the expected time.")
        
        time.sleep(wait_interval)
