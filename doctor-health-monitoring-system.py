class HealthMetrics:
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.vital_signs = {}

    def add_vital_sign(self, sign_name, value):
        self.vital_signs[sign_name] = value

    def get_vital_sign(self, sign_name):
        return self.vital_signs.get(sign_name, None)

    def display_metrics(self):
        print(f'Health Metrics for {self.patient_name}:')
        for sign, value in self.vital_signs.items():
            print(f'{sign}: {value}')

# Example usage in Python
if __name__ == '__main__':
    patient = HealthMetrics('John Doe')
    patient.add_vital_sign('Heart Rate', 72)
    patient.add_vital_sign('Blood Pressure', '120/80')
    patient.display_metrics()

// Example usage in JavaScript
class HealthMetricsJS {
    constructor(patientName) {
        this.patientName = patientName;
        this.vitalSigns = {};
    }

    addVitalSign(signName, value) {
        this.vitalSigns[signName] = value;
    }

    getVitalSign(signName) {
        return this.vitalSigns[signName] || null;
    }

    displayMetrics() {
        console.log(`Health Metrics for ${this.patientName}:`);
        for (const [sign, value] of Object.entries(this.vitalSigns)) {
            console.log(`${sign}: ${value}`);
        }
    }
}

// Example usage in JavaScript
const patientJS = new HealthMetricsJS('Jane Doe');
patientJS.addVitalSign('Heart Rate', 68);
patientJS.addVitalSign('Blood Pressure', '118/76');
patientJS.displayMetrics();