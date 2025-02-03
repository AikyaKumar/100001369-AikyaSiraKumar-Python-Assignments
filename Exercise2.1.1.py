import random
from datetime import datetime, timedelta

class CoronaPatientRecovery:
    def input(func):
        def innerFunction(*args, **kwargs):
        # Gather input values from the user
            recpat = int(input("Enter the number of recovered patients: "))
            batch_size = int(input("Enter the batch size of recovered patients: "))
            start_date = datetime(2020, 6, 1)
            end_date = datetime.today()
            return func(recpat, batch_size, start_date, end_date, *args, **kwargs)
        return innerFunction

    @staticmethod  
    @input
    def test(recpat, batch_size, start_date, end_date):
        batch = []
        batches = []

        # Create batches of patients
        for i in range(1, recpat + 1):
            patient = f"p{i}"
            batch.append(patient)

            if len(batch) == batch_size:
                batches.append(sorted(batch))
                batch = []

        if batch:  # Add remaining patients
            batches.append(sorted(batch))

        selected_p = set()
        test_dates = []
    
    # Select patients and assign random test dates
        for batch in batches:
            p_chosen = [p for p in batch if p not in selected_p]

            if p_chosen:
                p_choice = random.choice(p_chosen)
                selected_p.add(p_choice)

            # Generate a random test date
                no_days = (end_date - start_date).days
                random_days = random.randint(0, no_days)
                test_date = start_date + timedelta(days=random_days)
                test_dates.append((p_choice, test_date))

    # Sort test dates by date
        test_dates.sort(key=lambda x: x[1])

    # Display the results
        for patient, date in test_dates:
            print(f"The patient {patient} was tested on {date.strftime('%Y-%m-%d')}.")

patient = CoronaPatientRecovery()
patient.test()





