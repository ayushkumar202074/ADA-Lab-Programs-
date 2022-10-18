def job_sequencing(arr):
    arr.sort(key = lambda i:i[2], reverse=True)
    max_deadline = arr[0][2]
    
    job_execution = []
    
    for i in range(max_deadline):
        max_item = arr[0]
        for item in arr:
            if item[2] == i + 1 and item[1] > max_item[1]:
                max_item = item
        job_execution.append((max_item[0], max_item[1]))
    
    return job_execution

n = int(input("Enter number of jobs: "))
jobs = []

for i in range(n):
    job_id = input("Enter job id: ")
    arr = input("Enter the profit and deadline: ").split(" ")
    arr = [int(i) for i in arr]
    arr.insert(0, job_id)
    jobs.append(tuple(arr))

print(job_sequencing(jobs))