# health-dashboard.py

class HealthDashboard:
    def __init__(self):
        self.metrics = {}

    def add_metric(self, name, value):
        self.metrics[name] = value

    def get_metric(self, name):
        return self.metrics.get(name)

    def display_metrics(self):
        for name, value in self.metrics.items():
            print(f'{name}: {value}')

if __name__ == '__main__':
    dashboard = HealthDashboard()
    dashboard.add_metric('Heart Rate', '72 bpm')
    dashboard.add_metric('Blood Pressure', '120/80 mmHg')
    dashboard.add_metric('Oxygen Saturation', '98%')
    dashboard.display_metrics()