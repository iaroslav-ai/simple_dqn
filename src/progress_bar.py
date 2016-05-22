import sys as Sys
import time
# Print iterations progress
def printProgress (iteration, total, start_time = None, prefix = 'Progress: ', suffix = 'complete', decimals = 2, barLength = 30):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : number of decimals in percent complete (Int) 
        barLength   - Optional  : character length of bar (Int) 
    """
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '#' * filledLength + '-' * (barLength - filledLength)
    if start_time is None or percents == 0.0:
        Sys.stdout.write('%s [%s] %s%s %s\r' % (prefix, bar, percents, '%', suffix)),
    else:
        est_time = round((100.0 - percents) * (time.time() - start_time) / percents)
        Sys.stdout.write('%s [%s] %s%s %s %s\r' % (prefix, bar, percents, '%', est_time, "s remain   ")),
        
    Sys.stdout.flush()
    if iteration == total:
        print("\n")