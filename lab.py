#Luis F. Hernandez
#!/usr/bin/env python3
import time
import pymp

def wordsCount(keyword, thread):
    sum = pymp.shared.list([0])
    for i in range(1, 9):
        n = str(i)
        file = open('shakespeare'+n+'.txt','r')
        lines = file.readlines()
        file.close()
        with pymp.Parallel(thread) as p:
            dictRet = pymp.shared.dict()
            # get a lock for this parallel region
            sumLock = p.lock
            for line in p.iterate(lines):
                words = line.split(' ')
                for word in words:
                    # removing these locks leads to an incorrect sum
                    sumLock.acquire()
                    word = word.replace('\n', '')
                    word = word.replace(',', '')
                    word = word.replace('.', '')
                    word = word.replace(':', '')
                    word = word.replace(';', '')
                    if word.lower() == keyword:
                        sum[0] = sum[0] + 1
                    else:
                        pass

                    # removing just the release will result in
                    # deadlock
                    sumLock.release()





    dictRet['Number of '+keyword+' words in Shakespeare is: '] = sum[0]
    return dictRet

def main():
    """
    main function for when running as a script
    """
    numberOfThreads = [1, 2, 4, 8]
    for i in numberOfThreads:
        print("Number of threads: "+str(i))
        start = time.clock_gettime( time.CLOCK_MONOTONIC_RAW )
        newDict = wordsCount('hate', i)
        print(f'{newDict}')
        newDict = wordsCount('love', i)
        print(f'{newDict}')
        newDict = wordsCount('death', i)
        print(f'{newDict}')
        newDict = wordsCount('night', i)
        print(f'{newDict}')
        newDict = wordsCount('sleep', i)
        print(f'{newDict}')
        newDict = wordsCount('time', i)
        print(f'{newDict}')
        newDict = wordsCount('henry', i)
        print(f'{newDict}')
        newDict = wordsCount('hamlet', i)
        print(f'{newDict}')
        newDict = wordsCount('you', i)
        print(f'{newDict}')
        newDict = wordsCount('my', i)
        print(f'{newDict}')
        newDict = wordsCount('blood', i)
        print(f'{newDict}')
        newDict = wordsCount('poison', i)
        print(f'{newDict}')
        newDict = wordsCount('macbeth', i)
        print(f'{newDict}')
        newDict = wordsCount('king', i)
        print(f'{newDict}')
        newDict = wordsCount('heart', i)
        print(f'{newDict}')
        newDict = wordsCount('king', i)
        print(f'{newDict}')
        newDict = wordsCount('honest', i)
        print(f'{newDict}')
        end = time.clock_gettime( time.CLOCK_MONOTONIC_RAW )
        totalTime = end - start
        print(f'Elapsed Time: '+str(totalTime)+' Seconds')



if __name__ == '__main__':
    # execute only if run as a script
    main()
