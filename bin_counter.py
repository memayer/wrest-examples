from math import floor

class BinCounter:
    low = 0
    high = 0
    bins = []

    def __init__(self, input_low, input_high, num_bins):
        if input_high < input_low:
            raise ValueError("High cannot be lower than low.")
        if num_bins < 1 or type(num_bins) != int:
            raise ValueError("Number of bins must be a positive integer.")

        self.low = input_low
        self.high = input_high
        self.bins = []
        bin_size = int((self.high - self.low) / num_bins)

        # Create the bins
        tmp_low = self.low
        for x in range(0, num_bins):
            tmp_hash = {}
            tmp_hash['low'] = tmp_low
            tmp_hash['high'] = tmp_low + bin_size
            tmp_hash['values'] = []
            self.bins.append(tmp_hash)
            tmp_low = tmp_hash['high']

    # Insert a value in O(n) time
    def submit_value_linear(self, value):
        if value < self.low or value >= self.high:
            print "Value can't be lower than %s and must be lower than %s" % (self.low, self.high)
            return 0

        for x in range(0, len(self.bins)):
            if value < self.bins[x]['high']:
                # We'll allow duplicate values
                self.bins[x]['values'].append(value)
                return 1

        return 0

    # Insert a value in O(1) time
    def submit_value_constant(self, value):
        if value < self.low or value >= self.high:
            print "Value can't be lower than %s and must be lower than %s" % (self.low, self.high)
            return 0

        bin_size = int((self.high - self.low) / len(self.bins))
        bin_index = int(floor((value - self.low) / bin_size))
        self.bins[bin_index]['values'].append(value)

        return 1

    # Just use the constant time one as the generic
    def submit_value(self, value):
        return self.submit_value_constant(value)

    def print_bins(self):
        print "\nBins:"
        print "Absolute low:", self.low
        print "Absolute high:", self.high
        i = 0
        for x in self.bins:
            print "Bin", i
            print "Low %s, High %s, Values %s" % (x['low'], x['high'], x['values'])
            i += 1

# End BinCounter class


# Test it out
try:
    bad = BinCounter(5, 4, 3)
except ValueError as e:
    print "Nope,", e

foo = BinCounter(0, 5, 5)
foo.print_bins()
foo.submit_value_constant(8)
foo.submit_value_linear(5)
foo.submit_value_linear(0.2)
foo.submit_value_constant(0.5)
foo.submit_value_linear(2.7)
foo.submit_value_constant(4)
foo.submit_value_linear(4)
foo.print_bins()

bar = BinCounter(-1, 1, 2)
bar.print_bins()
bar.submit_value(-0.4)
bar.print_bins()

baz = BinCounter(-5.4, 6.3, 5)
baz.print_bins()
baz.submit_value(-2)
baz.submit_value(2.2)
baz.submit_value(1.61)
baz.submit_value(0.61)
baz.print_bins()

