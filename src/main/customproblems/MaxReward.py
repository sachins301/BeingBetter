"""
Optimization and Greedy Algorithm (Task Scheduling)

Problem: You have multiple tasks with different deadlines and rewards. Maximize the total reward by selecting tasks
within their respective deadlines.

MinimumLengthOfStringAfterOpertions_3223: Sort tasks by reward and use a greedy algorithm to select the highest reward tasks that can be completed
within their deadlines."""

def maxReward(tasks):
    # Sort tasks by reward in descending order
    tasks.sort(key=lambda x: -x[1])

    # Find the maximum deadline for the slot array
    maxslots = max(task[0] for task in tasks)
    slots = [False] * (maxslots + 1)
    totalreward = 0

    # Assign tasks to the latest possible slot up to their deadline
    for deadline, reward in tasks:
        for slot in range(deadline, 0, -1):
            if not slots[slot]:  # If the slot is available
                slots[slot] = True
                totalreward += reward
                break

    return totalreward

# Example usage:
tasks = [(3, 40), (1, 20), (2, 50), (2, 10)]
print(maxReward(tasks))  # Expected Output: 90
