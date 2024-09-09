def gradient(height, start, stop):
    table = []
    for y in range(height):
        progress = y / (height - 1)
        color = tuple(int(start[i] * (1 - progress) + stop[i] * progress) for i in range(3))
        color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        table.append(f'<td style="background-color: {color.upper()}; width:500px; height:2px;"></td>')
    return table

table = gradient(1024, (255, 255, 255), (0, 0, 0))

html_table = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Gradient Table</title>
    <style>
        table {{
            border-collapse: collapse;
        }}
    </style>
</head>
<body>
    <table>
        {"".join([f'<tr>{"".join(row)}</tr>' for row in table])}
    </table>
</body>
</html>
"""
with open("color_gradient_table.html", "w", encoding="utf-8") as file:
    file.write(html_table)
