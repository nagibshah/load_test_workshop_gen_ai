from locust import HttpUser, task

class GenAiProxyUser(HttpUser):
    @task
    def prompt(self):
        self.client.post("/invoke")