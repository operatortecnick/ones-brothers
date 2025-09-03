# Minimal mock for schedule module for testing
class Job:
    def do(self, job_func):
        return self
    
    def at(self, time_str):
        return self

class Schedule:
    def every(self):
        return MockEvery()
    
    def run_pending(self):
        pass

class MockEvery:
    @property
    def day(self):
        return Job()

schedule = Schedule()

def run_pending():
    pass