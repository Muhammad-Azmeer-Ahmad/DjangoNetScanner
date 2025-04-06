from django.shortcuts import render
import subprocess

def index(request):
    return render(request, 'index.html')

def scan_target(request):
    if request.method == "POST":
        target = request.POST.get('target')
        if not target:
            return render(request, 'index.html', {'error': 'No target provided'})

        try:
            # Run Nmap scan (Optimized for faster results)
            result = subprocess.run(
                ["nmap", "-F", "-T5", target],  # -F (Fast mode), -T5 (Aggressive timing)
                capture_output=True, text=True
            )

            if result.returncode != 0:
                return render(request, 'index.html', {'error': 'Error fetching scan data.'})

            scan_data = result.stdout.strip()
            if not scan_data:
                return render(request, 'index.html', {'error': 'No scan results found.'})

            return render(request, 'index.html', {'scan_data': scan_data})

        except Exception as e:
            return render(request, 'index.html', {'error': f'Error: {str(e)}'})

    return render(request, 'index.html')
