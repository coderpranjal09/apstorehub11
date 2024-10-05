import tkinter as tk
from tkinter import messagebox

class FinanceManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Management System")

        # Initialize data
        self.clients = {}
        self.workers = {}
        self.company_balance = 0
        self.total_worker_payout = 0
        self.costs = 0

        # Create the GUI
        self.create_gui()

    def create_gui(self):
        # Company Balance
        tk.Label(self.root, text="Company Balance:").grid(row=0, column=0, padx=10, pady=10)
        self.company_balance_entry = tk.Entry(self.root)
        self.company_balance_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Add Client Section
        tk.Label(self.root, text="Client Name:").grid(row=1, column=0, padx=10, pady=10)
        self.client_name_entry = tk.Entry(self.root)
        self.client_name_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Due Amount:").grid(row=2, column=0, padx=10, pady=10)
        self.due_amount_entry = tk.Entry(self.root)
        self.due_amount_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Add Client", command=self.add_client).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Add Worker Section
        tk.Label(self.root, text="Worker Name:").grid(row=4, column=0, padx=10, pady=10)
        self.worker_name_entry = tk.Entry(self.root)
        self.worker_name_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Salary:").grid(row=5, column=0, padx=10, pady=10)
        self.worker_salary_entry = tk.Entry(self.root)
        self.worker_salary_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Add Worker", command=self.add_worker).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # View Stats Section
        tk.Button(self.root, text="View Company Stats", command=self.view_stats).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_client(self):
        client_name = self.client_name_entry.get()
        try:
            due_amount = float(self.due_amount_entry.get())
            if client_name:
                self.clients[client_name] = {'due': due_amount, 'paid': 0}
                messagebox.showinfo("Success", f"Client {client_name} added with a due amount of {due_amount}.")
                self.clear_client_entries()
            else:
                messagebox.showerror("Error", "Client name cannot be empty.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid due amount.")

    def add_worker(self):
        worker_name = self.worker_name_entry.get()
        try:
            salary = float(self.worker_salary_entry.get())
            if worker_name:
                self.workers[worker_name] = salary
                messagebox.showinfo("Success", f"Worker {worker_name} added with a salary of {salary}.")
                self.clear_worker_entries()
            else:
                messagebox.showerror("Error", "Worker name cannot be empty.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid salary.")

    def view_stats(self):
        try:
            self.company_balance = float(self.company_balance_entry.get())
            total_due = sum(client['due'] for client in self.clients.values())
            total_paid = sum(client['paid'] for client in self.clients.values())
            total_salary = sum(self.workers.values())

            stats = f"""
            Company Balance: {self.company_balance}
            Total Due from Clients: {total_due}
            Total Paid by Clients: {total_paid}
            Total Salaries to Workers: {total_salary}
            Net Worth: {self.company_balance - total_salary}
            """
            messagebox.showinfo("Company Stats", stats)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid company balance.")

    def clear_client_entries(self):
        self.client_name_entry.delete(0, tk.END)
        self.due_amount_entry.delete(0, tk.END)

    def clear_worker_entries(self):
        self.worker_name_entry.delete(0, tk.END)
        self.worker_salary_entry.delete(0, tk.END)

# Main loop to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceManagerApp(root)
    root.mainloop()
