from rich.console import Console
from rich.table import Table

console = Console()

def print_job_start(job_id, prompt, plugin_name):
    console.print(f"[bold cyan]▶ Starting Job:[/bold cyan] {job_id} | Plugin: [magenta]{plugin_name}[/magenta]", highlight=False)
    console.print(f"[dim]Prompt:[/dim] {prompt}\n")

def print_job_result(job_id, status, duration):
    color = "green" if status == "completed" else "red"
    console.print(f"[bold {color}]✓ Job {job_id} {status.upper()}[/bold {color}] ({duration})\n")

def print_summary(total, completed, failed, skipped):
    table = Table(title="Render Summary")
    table.add_column("Total", style="bold")
    table.add_column("Completed", style="green")
    table.add_column("Failed", style="red")
    table.add_column("Skipped", style="yellow")
    table.add_row(str(total), str(completed), str(failed), str(skipped))
    console.print(table)
