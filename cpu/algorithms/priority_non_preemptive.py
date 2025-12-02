def priority_non_preemptive(processes, priorities):
    """
    Implement Priority Non-Preemptive CPU scheduling algorithm
    
    Priority Non-Preemptive is a scheduling algorithm where processes are executed 
    based on their priority (higher priority first) without preemption.
    When multiple processes are available, the one with highest priority is selected.
    
    Args:
        processes: List of tuples where each tuple represents a process
                  Format: (process_id, arrival_time, burst_time)
        priorities: Dictionary mapping process_id to priority value
                   Format: {pid: priority}
                   Note: Higher value = Higher priority
    
    Returns:
        tuple: (gantt_chart, waiting_times, turnaround_times, completion_times)
        - gantt_chart: List of tuples (pid, start_time, end_time)
        - waiting_times: Dictionary {pid: waiting_time}
        - turnaround_times: Dictionary {pid: turnaround_time}
        - completion_times: Dictionary {pid: completion_time}
    """
    
    if not processes:
        return [], {}, {}, {}
    
    # Step 1 - Sort processes by arrival time initially
    processes = sorted(processes, key=lambda p: p[1])
    
    # Step 2 - Initialize variables
    gantt_chart = []
    waiting_times = {}
    turnaround_times = {}
    completion_times = {}
    
    current_time = 0
    completed = 0
    n = len(processes)
    
    # Track remaining processes
    remaining_processes = []
    for pid, arrival, burst in processes:
        remaining_processes.append({
            'pid': pid,
            'arrival': arrival,
            'burst': burst,
            'priority': priorities.get(pid, 0),
            'completed': False
        })
    
    # Step 3 - Process scheduling loop
    while completed < n:
        # Find available processes
        available = [p for p in remaining_processes 
                    if not p['completed'] and p['arrival'] <= current_time]
        
        # If no process available, jump to next arrival
        if not available:
            next_arrival = min([p['arrival'] for p in remaining_processes 
                              if not p['completed']])
            current_time = next_arrival
            continue
        
        # Select process with highest priority (higher number = higher priority)
        # For tie-breaking: higher priority first, then earlier arrival
        selected = max(available, key=lambda p: (p['priority'], -p['arrival']))
        
        # Execute selected process
        start_time = current_time
        end_time = start_time + selected['burst']
        
        # Add to Gantt chart
        gantt_chart.append((selected['pid'], start_time, end_time))
        
        # Calculate metrics
        completion_time = end_time
        turnaround_time = completion_time - selected['arrival']
        waiting_time = turnaround_time - selected['burst']
        
        # Store results
        completion_times[selected['pid']] = completion_time
        turnaround_times[selected['pid']] = turnaround_time
        waiting_times[selected['pid']] = waiting_time
        
        # Update state
        current_time = end_time
        selected['completed'] = True
        completed += 1
    
    # Step 4 - Return results
    return gantt_chart, waiting_times, turnaround_times, completion_times
