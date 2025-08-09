import statistics

def input_data():
    while True:
        data_str = input("Please enter integers separated by spaces: ").split()
        try:
            data_int = list(map(int, data_str))
            if len(data_int) == 0:
                print("Empty list is not allowed. Try again.")
            else:
                return data_int
        except ValueError:
            print("Invalid input! Please enter integers only.")


def calculate_basic_stats(data):
    stats = dict()
    stats["mean"] = statistics.mean(data)
    stats["median"] = statistics.median(data)
    stats["variance"] = statistics.variance(data)
    stats["stdev"] = statistics.stdev(data)

    try:
        stats["mode"] = statistics.mode(data)
    except statistics.StatisticsError:
        stats["mode"] = "No unique mode"

    return stats


def calculate_z_scores(data, mean, stdev):
    if stdev == 0:
        print("Standard deviation is zero, z-score cannot be calculated.")
        return []

    z_scores = [(x - mean) / stdev for x in data]
    return z_scores
