# algorithms/fcfs.py

def fcfs(processes):
    """
    TODO: Implement First-Come, First-Served (FCFS) CPU scheduling algorithm
    
    FCFS is a non-preemptive scheduling algorithm where processes are executed 
    in the order of their arrival time.
    
    Args:
        processes: List of tuples where each tuple represents a process
                  Format: (process_id, arrival_time, burst_time)
    
    Returns:
        tuple: (gantt_chart, waiting_times, turnaround_times, completion_times)
        - gantt_chart: List of tuples (pid, start_time, end_time)
        - waiting_times: Dictionary {pid: waiting_time}
        - turnaround_times: Dictionary {pid: turnaround_time}
        - completion_times: Dictionary {pid: completion_time}
    """
    
    # TODO: 
    # Currently returning empty data - replace with your implementation
    
    gantt_chart = []
    waiting_times = {}
    turnaround_times = {}
    completion_times = {}
    
    # TODO: Step 1 - Sort processes by arrival time
        processes = sorted(processes, key=lambda p: p[1])  # p[1] = arrival_time
    # TODO: Step 2 - Initialize current_time
        current_time = 0
    # TODO: Step 3 - Process each job in FCFS order
     for pid, arrival, burst in processes:

        if current_time < arrival:
            current_time = arrival

        start_time = current_time
        end_time = start_time + burst
           # Fill gantt chart
        gantt_chart.append((pid, start_time, end_time))

        # Fill timing results
        completion_times[pid] = end_time
        turnaround_times[pid] = end_time - arrival
        waiting_times[pid] = start_time - arrival

        current_time = end_time
    # TODO: Step 4 - Return the results
    
    return gantt_chart, waiting_times, turnaround_times, completion_times
