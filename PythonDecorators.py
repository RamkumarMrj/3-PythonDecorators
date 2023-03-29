def log_message(func):
    def wrapper(*args, **kwargs):
       
        result = func(*args, **kwargs)
      
        with open('/tmp/decorator_logs.txt', 'a') as f:
      
            f.write(result + '\n')
       
        return result
    return wrapper

@log_message
def a_function_that_returns_a_string():
    return "A string"

@log_message
def a_function_that_returns_a_string_with_newline(s):
    return "{}\n".format(s)

@log_message
def a_function_that_returns_another_string(string=""):
    return "Another string"
