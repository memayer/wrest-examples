# An example to demonstrate using decorators

call_counts = {}

def call_counter(func):
    global call_counts
    def inner(*args, **kwargs):
        if func.__name__ in call_counts.keys():
            call_counts[func.__name__] += 1
        else:
            call_counts[func.__name__] = 1

        return func(*args, **kwargs)

    return inner

@call_counter
def foo(x):
    print x

@call_counter
def bar(x, y):
    print "%s, %s" % (x, y)

@call_counter
def baz(dct):
    for key in dct.keys():
        print "%s : %s" % (key, dct[key])

print "Before calling anything:"
print call_counts, "\n"

foo(1)
bar(1, 1)
baz({'one' : 1})

print "After calling each function once:"
print call_counts, "\n"

foo("Let's Go Blues!")
foo("Michael rules")
baz({'Stanley Cup Winners' : 'St. Louis Blues', 'World Series Winners' : 'St. Louis Cardinals'})

print "After calling foo 2 more times and baz once more:"
print call_counts

