#Lizzy Saldana Debugging notes
import trace
import sys
tracer = trace.Trace(count=False, trace=True)
def trace_calls(frame, event, arg):
    if event == 'call':#when function is called
        print(f'calling function: {frame.f_code.co_name}')
    elif event == "line": #happens when a new line of code happens
        print(f"Executing line {frame.f_lineno} in {frame.f_code.co_name}")
    elif event == 'return': #Checks when we return stuff
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exceptions': #When there are issues
        print(f'exception in {frame.f_code.co_name}: {arg}')
    return trace_calls

sys.settrace(trace_calls)

"""What is tracing?
    it allows you to access information about the functions in your program.
    Basic Tracing command:
    python -m trace --trace FILEPATH
    --trace (displays lines as executed)
    --count (displays number of times its executed)
    --listfuncs (displays the functions executed by running program)
    --trackcalls (tells us the relationship between the functions)
    """ 

def sub(x,y):
    return x-y

def add(x,y):
    print(sub(x,y))
    return x+y

print(add(5,2))


#tracer.run
"""
What are some ways we can debug by tracing?
    we can use tracing to help us find where errors are ocurring. Helps us observe what our program is doing without disrupting it.
How do you access the debugger in VS Code?
    press f5, or press the debug button on the left, or go to the drop down and presss debug
What is testing?
    Testing is running your code to make sure it works as required.
What are boundary conditions?
    checking the edge possibilities to make sure they work properly
How do you handle when users give strange inputs?
    try and except,  basic conditionals and loops.

"""