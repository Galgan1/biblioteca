import subprocess, sys, os

scripts_dir = os.path.join(sys.prefix, "Scripts")
marker_exe = os.path.join(scripts_dir, "marker_single.exe")

if not os.path.exists(marker_exe):
    marker_exe = os.path.join(scripts_dir, "marker.exe")

output_dir = r"C:\Users\User\AppData\Local\Temp\book_skill_work\marker_output"
os.makedirs(output_dir, exist_ok=True)

pdf_path = r"C:\Users\User\Downloads\Robert McKee - Story (pdf).pdf"

# Run with NO timeout this time, GPU CUDA should make it much faster
cmd = [marker_exe, pdf_path, "--output_dir", output_dir, "--output_format", "markdown"]
print(f"Running: {' '.join(cmd)}")
print(f"GPU CUDA enabled - this should be MUCH faster now!")
result = subprocess.run(cmd, capture_output=True, text=True)
print("STDOUT:", result.stdout[-3000:] if len(result.stdout) > 3000 else result.stdout)
if result.stderr:
    print("STDERR:", result.stderr[-2000:] if len(result.stderr) > 2000 else result.stderr)
print("Return code:", result.returncode)
