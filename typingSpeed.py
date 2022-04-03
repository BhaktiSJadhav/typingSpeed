from time import time


def tperror(prompt):
    global inwords
    
    words = prompt.split()
    errors = 0
    
    for i in range (len(inwords)):
        if i in range(0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else :
            if inwords[i] == words[i]:

                if(inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors
    
    
def speed(inprompt, stime, etime):
    global time
    global inwords
    
    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time
    
    return speed

def elapsedtime(stime,etime):
    time = etime - stime
    return time


if __name__ == '__main__':
    prompt = "python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming.Python is often described as a batteries included language due to its comprehensive standard library."
    
    print("Type this:- ",prompt,"")
          
          
    input("Press Enter when you are ready to check your speed!!!")
    
    stime = time()
    inprompt = input()
    etime = time()      
    
    time = round(elapsedtime(stime,etime),2)    
    speed = speed(inprompt,stime,etime)
    errors = tperror(prompt)
    
    print("#####################################")
    print("Total time elapsed: ", time, "seconds")
    print("Your Average Typing speed was", speed, "words per minute (w/m)")
    print("with the total of ", errors, "errors")
    print("#####################################")   