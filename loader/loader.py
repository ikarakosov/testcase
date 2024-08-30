from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def status(self):
        self.client.get("/status")

    @task(2)
    def wait(self):
        self.client.get("/wait")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Wait time between tasks, in seconds

if __name__ == "__main__":
    import locust
    locust.run_single_user(WebsiteUser)
