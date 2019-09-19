"""
You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.

Example:
{
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}

This input should return the order that we need to take these courses:
 ['CSC100', 'CSC200', 'CSCS300']

Here's your starting point:

"""


def courses_to_take(courses_dict):
    order = []
    for value in courses_dict:
        if not courses_dict[value]:
            order.append(value)

    for value in order:
        del courses_dict[value]

    for key, value in courses_dict.items():
        for val in value:
            if val not in order:
                order.append(val)
        if key not in order:
            order.append(key)

    return order


courses = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': [],
}
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
