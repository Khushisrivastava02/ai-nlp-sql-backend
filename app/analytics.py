queries = []

def log_query(question, execution_time):
    queries.append((question, execution_time))

def get_stats():
    total_queries = len(queries)

    if total_queries == 0:
        slowest = None
    else:
        slowest = max(queries, key=lambda x: x[1])

    return {
        "total_queries": total_queries,
        "slowest_query": slowest
    }