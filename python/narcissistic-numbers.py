def narcissistic(value):
    raised = [int(i) ** len(str(value)) for i in str(value)]
    return value == sum(raised)
