import loggerjava
if __name__ == "__main__":pass

loggerjava.config(debuginanotherfile = True)
loggerjava.clearcurrentlog()
loggerjava.info('test')
loggerjava.warn('test',pos='test?')
loggerjava.debug('test!')
