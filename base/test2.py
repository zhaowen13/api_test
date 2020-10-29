# import test

def my_run(fn):
    # @test.spamrun
    def sayspam(*args):
        # print("spam,spam,spam")
        fn(*args)
        pass
    return sayspam

def attrs(**kwds):
    def decorate(f):
        return f
    print(kwds['versionadded'])

    return decorate


@attrs(versionadded="2.2",author="Guido van Rossum")
def mymethod(f):
    # print(getattr(mymethod,'versionadded',0))
    # print(getattr(mymethod,'author',0))
    print(f)

if __name__ == "__main__":
    mymethod(2)  