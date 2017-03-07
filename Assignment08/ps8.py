# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    subjects = {}
    # value = 0
    # work = 0
    for line in inputFile:
        parseLine = line.split(',')
        # value += int(parseLine[1].strip())
        # work += int(parseLine[2].strip())
        subjects[parseLine[0].strip()] = (int(parseLine[1].strip()), int(parseLine[2].strip()))
    # print value, work
    return subjects

subjects = loadSubjects(SUBJECT_FILENAME)
# print subjects

    # Done: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization

# ans = {}

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # or using merge sort to sort the qualified name list according to comparator first
    smallCatalog = {}
    for key in subjects.keys():
        if subjects[key][WORK] <= maxWork:
            smallCatalog[key] = subjects[key]
    if len(smallCatalog) == 0:
        return ans
    # print smallCatalog

    name = smallCatalog.keys()
    name.sort()
    # print name
    index1, index2 = 0, 1
    ans_index = 0
    while index2 < len(name):
        if comparator(smallCatalog[name[index1]], smallCatalog[name[index2]]):
            ans_index = index1
        else:
            ans_index = index2
            index1 = index2
        # print ans_index
        index2 += 1
    used_work = int(smallCatalog[name[ans_index]][WORK])
    ans[name[ans_index]] = smallCatalog[name[ans_index]]
    del smallCatalog[name[ans_index]]
    return greedyAdvisor(smallCatalog, maxWork - used_work, comparator)

# selected = greedyAdvisor(subjects, 6, cmpValue)
# printSubjects(selected)




    # DONE...

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    start_time = time.time()
    print bruteForceAdvisor(subjects, 10)
    end_time = time.time()
    return end_time - start_time

# print bruteForceTime()
    # Done...

# Problem 3 Observations
# ======================
#
# DONE: write here your observations regarding bruteForceTime's performance
# when maxWork = 9, time used = 17.00 secs.
# #When maxWork = 10, time used = 46.76 secs, which, I think, is an unreasonable amount of time.

#
# Problem 4: Subject Selection By Dynamic Programming
#



# def maxVal(subjects, maxWork, name, i, m):
#     try: return m[(i, maxWork)]
#     except:
#         if i == 0:
#             if subjects[name[i]][WORK] <= maxWork:
#                 m[(i, maxWork)] = subjects[name[i]][VALUE]
#                 return subjects[name[i]][VALUE]
#             else:
#                 m[(i, maxWork)] = 0
#                 return 0
#         without_i = maxVal(subjects, maxWork, name, i-1, m)
#         if subjects[name[i]][WORK] > maxWork:
#             m[(i, maxWork)] = without_i
#             return without_i
#         else: with_i = subjects[name[i]][VALUE] + maxVal(subjects, maxWork - subjects[name[i]][WORK], name, i-1, m)
#         res = max(with_i, without_i)
#         m[(i, maxWork)] = res
#         return res
#
#
# def dpAdvisor(subjects, maxWork):
#     """
#     Returns a dictionary mapping subject name to (value, work) that contains a
#     set of subjects that provides the maximum value without exceeding maxWork.
#
#     subjects: dictionary mapping subject name to (value, work)
#     maxWork: int >= 0
#     returns: dictionary mapping subject name to (value, work)
#     """
#     m = {}
#     name = subjects.keys()
#     i = len(name) - 1
#     return maxVal(subjects, maxWork, name, i, m)



def maxVal(subjects, maxWork, name, i, m):
    try: return m[(i, maxWork)]
    except:
        if i == 0:
            if subjects[name[i]][WORK] <= maxWork:
                m[(i, maxWork)] = subjects[name[i]][VALUE], [i]
                return subjects[name[i]][VALUE], [i]
            else:
                m[(i, maxWork)] = 0, []
                return 0, []
        without_i, selected = maxVal(subjects, maxWork, name, i-1, m)
        if subjects[name[i]][WORK] > maxWork:
            m[(i, maxWork)] = without_i, selected
            return without_i, selected
        else:
            with_i, selected_temp = maxVal(subjects, maxWork - subjects[name[i]][WORK], name, i-1, m)
            with_i += subjects[name[i]][VALUE]
        if with_i > without_i:
            selected = [i] + selected_temp
        res = max(with_i, without_i)
        m[(i, maxWork)] = res, selected
        return res, selected


def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    m = {}
    selected_dict = {}
    name = subjects.keys()
    i = len(name) - 1
    totalvalue, selected_list = maxVal(subjects, maxWork, name, i, m)
    for index in selected_list:
        selected_dict[name[index]] = subjects[name[index]]
    return selected_dict

# print dpAdvisor(subjects, 30)
printSubjects(dpAdvisor(subjects, 30))
    # TODO...




# def dpAdvisor(subjects, maxWork):
#     """
#     Returns a dictionary mapping subject name to (value, work) that contains a
#     set of subjects that provides the maximum value without exceeding maxWork.
#
#     subjects: dictionary mapping subject name to (value, work)
#     maxWork: int >= 0
#     returns: dictionary mapping subject name to (value, work)
#
#     These are the results for running this full catalog:
#     {8: 0.02, 10: 0.01, 45: 0.080000000000000002, 15: 0.02, 120: 0.23000000000000001, 90: 0.23000000000000001, 60: 0.11, 30: 0.050000000000000003}
#
#     """
#     # TODO...
#
#     rec_dict = {}
#     m = {}
#
#     #   Build the work and value lists.
#     work_list = []
#     value_list = []
#     key_list = []
#     for each in subjects:
#         work_list.append(subjects[each][1])
#         value_list.append(subjects[each][0])
#         key_list.append(each)
#
#     # Build optimal list of courses to take.
#     value, rec_list = dp_decision_tree(work_list, value_list, len(work_list) - 1, maxWork, m)
#
#     #   Build dictionary from list.
#     for each in rec_list:
#         rec_dict[key_list[each]] = (value_list[each], work_list[each])
#     return rec_dict
#
#
# def dp_decision_tree(w, v, i, aW, m):
#     """
#     Creates a course schedule that is optimized the maximum value.
#     """
#
#     ## check if value is already in the dictionary
#     try:
#         return m[(i, aW)]
#     except KeyError:
#         ##  Leaf/Bottom of the tree case decision
#         if i == 0:
#             if w[i] < aW:
#                 m[(i, aW)] = v[i], [i]
#                 return v[i], [i]
#             else:
#                 m[(i, aW)] = 0, []
#                 return 0, []
#
#     ## Calculate with and without i branches
#     without_i, course_list = dp_decision_tree(w, v, i - 1, aW, m)
#     if w[i] > aW:
#         m[(i, aW)] = without_i, course_list
#         return without_i, course_list
#     else:
#         with_i, course_list_temp = dp_decision_tree(w, v, i - 1, aW - w[i], m)
#         with_i += v[i]
#
#     ## Take the branch with the higher value
#     if with_i > without_i:
#         i_value = with_i
#         course_list = [i] + course_list_temp
#     else:
#         i_value = without_i
#
#     ## Add this value calculation to the memo
#     m[(i, aW)] = i_value, course_list
#     return i_value, course_list
#
#
# printSubjects(dpAdvisor(subjects, 30))






#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
