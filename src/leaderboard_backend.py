import os

class Backend:
    """Handles data processing and file operations"""
    
    def __init__(self):
        # Create 'leaderboard' folder in the root if it doesn't exist
        self.leaderboard_dir = os.path.join(os.getcwd(), 'leaderboard')
        os.makedirs(self.leaderboard_dir, exist_ok=True)
        self.html_file = os.path.join(self.leaderboard_dir, "leaderboard.html")

    def update_leaderboard(self, data):
        """Main method to update leaderboard"""
        self._clean_old_file()
        sorted_runners = self._process_data(data)
        html_content = self._generate_html_content(sorted_runners)
        self._write_html_file(html_content)

    def _clean_old_file(self):
        """Removes existing leaderboard file"""
        try:
            os.remove(self.html_file)
        except FileNotFoundError:
            pass

    def _process_data(self, data):
        """Processes and sorts runner data"""
        valid_runners = [runner for runner in data if runner['time'] != '00:00.0']
        invalid_runners = [runner for runner in data if runner['time'] == '00:00.0']
        
        sorted_valid = sorted(valid_runners, key=lambda x: self._time_to_seconds(x['time']))
        sorted_invalid = sorted(invalid_runners, key=lambda x: x['nickname'].lower())
        return sorted_valid + sorted_invalid

    def _generate_html_content(self, runners):
        """Generates HTML structure"""
        html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Leaderboard</title>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * { 
      box-sizing: border-box; 
      margin: 0; 
      padding: 0; 
      font-family: 'Montserrat', sans-serif;
    }
    body { color: #fff; }
    .leaderboard { display: flex; width: 100%; border-bottom: 2px solid #fff; }
    .leaderboard .position { flex: 1; display: flex; flex-direction: column; 
      align-items: center; justify-content: center; border-left: 2px solid #fff; 
      padding: 4px; white-space: nowrap; }
    .leaderboard .position:first-of-type { border-left: none; }
    .placement-name { font-size: 14px; font-weight: 700; }
    .perf-time { font-size: 16px; margin-top: 4px; }
  </style>
</head>
<body>
  <div class="leaderboard">\n'''
        
        for rank, runner in enumerate(runners, 1):
            ordinal = self._get_ordinal(rank)
            html_content += f'''    <div class="position">
      <div class="placement-name">{ordinal} - {runner['nickname']}</div>
      <div class="perf-time">{runner['time']}</div>
    </div>\n'''
        
        html_content += '''  </div>
</body>
</html>'''
        return html_content

    def _write_html_file(self, content):
        """Writes content to file with auto-reload"""
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        with open(self.html_file, 'a', encoding='utf-8') as f:
            f.write("""
                <script>
                window.location.reload(true);
                </script>
            </body>
            </html>
            """)

    @staticmethod
    def _time_to_seconds(time_str):
        """Converts time string to seconds"""
        try:
            minutes, rest = time_str.split(':')
            seconds, tenths = rest.split('.')
            return int(minutes) * 60 + float(f"{seconds}.{tenths}")
        except ValueError:
            return float('inf')

    @staticmethod
    def _get_ordinal(num):
        # Generate ordinal suffix (st/nd/rd/th) for numbers
        # Handles special cases 11-13 (all use 'th') and general cases (1st, 2nd, 3rd, 4th, etc)
        # Logic: 
        # - For numbers where last two digits are 11-19: always use 'th'
        # - For other numbers: use last digit to determine suffix
        # - suffixes dictionary contains special cases {1: 'st', 2: 'nd', 3: 'rd'}
        # - Defaults to 'th' if no match found in suffixes
        suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
        return f"{num}{suffixes.get(num if (num % 100) < 20 else num % 10, 'th')}"