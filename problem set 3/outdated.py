months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        # Format: MM/DD/YYYY
        if "/" in date:
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)

        # Format: Month DD, YYYY
        else:
            parts = date.replace(",", "").split()
            m = months.index(parts[0]) + 1
            d = int(parts[1])
            y = int(parts[2])

        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y:04d}-{m:02d}-{d:02d}")
            break

    except (ValueError, IndexError):
        continue