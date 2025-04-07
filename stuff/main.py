import matplotlib.pyplot as plt

def pie_charts(expense):
    # Get user data and expense category
    one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve = info()
    
    # Define expense categories
    if expense == 'Budgeting':
        labels = ['Savings', 'House', 'Utilities', 'Insurance', 'Food', 'Entertainment', 'Healthcare', 'Phone', 'Pet']
        expenses = [one, two, three, four, five, six, seven, eight, nine]
    elif expense == 'Services':
        labels = ['Utilities' ,'Insurance', 'food', 'Entertainment','Healthcare','Phone']
        expenses = [one, two, three, four, five, six]
    elif expense == 'All':
        labels = ['Checkings','Salary','Goal','Savings', 'House', 'Utilities', 'Insurance', 'Food', 'Entertainment', 'Healthcare', 'Phone', 'Pet']
        expenses = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]
    
    # Plotting the pie chart
    fig, ax = plt.subplots()
    ax.pie(expenses, labels=labels, autopct='%1.1f%%')
    plt.title(f"Expense: {expense}")
    plt.show()


