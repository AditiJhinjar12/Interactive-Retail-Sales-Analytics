import os
import json
import random
from datetime import datetime, timedelta

# Create realistic sample Kaggle Superstore rows
random.seed(42)

subcategories = {
    "Furniture": ["Bookcases", "Chairs", "Tables", "Furnishings"],
    "Office Supplies": ["Labels", "Art", "Paper", "Binders", "Storage", "Appliances", "Fasteners", "Supplies", "Envelopes"],
    "Technology": ["Phones", "Accessories", "Copiers", "Machines"]
}

sample_products = {
    "Bookcases": ["Bush Somerset Collection Bookcase", "Sauder Heritage Hill 5-Shelf Bookcase", "Riverside Palais Royal Lawyers Bookcase", "Atlantic Magazine Storage Shelf Rack", "O'Sullivan 2-Shelf Adjustable Bookcase"],
    "Chairs": ["Hon Deluxe Fabric Upholstered Stacking Chairs", "Herman Miller Aeron Ergonomic Office Chair", "Steelcase Gesture Ergonomic Office Chair", "Global High Back Tilter Chair", "Novimex Swivel Mesh Task Chair", "Harbour Creations Executive Chair"],
    "Tables": ["Bretford CR4500 Series Slim Rectangular Table", "Chromcraft Bull-Nose Wood Oval Conference Tables", "Balt Solid Wood Workstation Training Table", "BPI Wood Laminate Conference Table 96x42", "Boxer Modern Wood End Table 2-Pack", "Bevis Round Conference Table"],
    "Furnishings": ["Eldon Expressions Wood Desk Accessories", "Seth Thomas Executive Wall Clock", "DAX Clear Document Frame", "Deflect-o Desk Pad", "Nu-Dell Wood Desk Tray"],
    "Labels": ["Self-Adhesive Address Labels for Laser Printers", "Avery 5160 Easy Peel Address Labels", "Avery File Folder Labels", "Dot Matrix Heavy Duty Labels"],
    "Art": ["Newell 322", "Prismacolor Premiere Colored Pencils 72-Set", "Boston School Pro Electric Pencil Sharpener", "Fiskars Recycled Scissors", "Sanford Liquid Accent Highlighters"],
    "Paper": ["Xerox 1967", "Xerox 205 Premium Multipurpose Paper", "Hammermill Premium Laser Print Paper", "Xerox 1980 High Performance Color Paper", "Southworth 25% Cotton Resume Paper"],
    "Binders": ["Avery Non-Stick Heavy Duty Ring Binders", "GBC VeloBind System Two Electric Punch Bind", "Wilson Jones Continuous Form Binder", "Fellowes Binding Combs 3/8in", "Acco Flexible Heavy-Duty Prong Fasteners"],
    "Storage": ["Fellowes Bankers Box Stor/Drawer Steel Plus", "Adjustable Heavy-Duty Wire Shelving Unit", "Safco Executive Mobile File Cart", "Tennsco Deluxe Steel Storage Cabinet 78H", "Iris Plastic Utility Storage Bins"],
    "Appliances": ["Avanti Single-Door Compact Refrigerator", "Cuisinart Microwave Oven w/ Grill", "Honeywell True HEPA Air Purifier HPA300", "Fellowes Powershred 99Ci Paper Shredder", "Hamilton Beach Commercial Toaster"],
    "Fasteners": ["Staples Box Binder Clips", "Advantus Push Pins Plastic Head", "Swingline Heavy-Duty Desk Stapler", "OIC Steel Paper Clips"],
    "Supplies": ["Fiskars Commercial Grade Rotary Trimmer", "Acme Forged Carbon Steel Scissors", "Stabila 24-Inch Magnetic Level", "Helix Stainless Steel Ruler"],
    "Envelopes": ["Self-Seal White Catalog Envelopes #10", "Tyvek Tear-Proof Expandable Envelopes", "Brown Kraft Clasp Envelopes 9x12", "Redi-Seal Security Tint Envelopes"],
    "Phones": ["Mitel 5320 IP Phone", "Apple iPhone 14 128GB Midnight", "Samsung Galaxy S23 Ultra 512GB", "Google Pixel 8 Pro 256GB", "Polycom SoundPoint Pro SE-225 Phone", "Apple iPhone 15 Pro Max 256GB"],
    "Accessories": ["Logitech Wireless Gaming Headset G930", "Keychron Q1 Pro Custom Mechanical Keyboard", "Dell UltraSharp 32-inch 4K Monitor", "Logitech MX Master 3S Wireless Mouse", "Bose QuietComfort 45 Headphones", "SanDisk Ultra 128GB MicroSDXC UHS-I"],
    "Copiers": ["Canon ImageCLASS 2200 Advanced Copier", "Hewlett Packard LaserJet Multifunction Copier", "Canon imageRUNNER ADVANCE C5535i Copier", "Sharp AL-1530CS Digital Copier", "Canon imageCLASS MF743Cdw All-in-One"],
    "Machines": ["Bady Automated Thermal Label Printer", "Zebra GX430t Thermal Direct Desktop Printer", "HP DesignJet Large-Format Color Plotter", "Epson WorkForce Pro WF-C5790", "Star Micronics TSP143III Receipt Printer"]
}

regions_states = {
    "West": [("California", ["Los Angeles", "San Francisco", "San Diego", "San Jose", "Sacramento"]),
             ("Washington", ["Seattle", "Spokane", "Tacoma"]),
             ("Utah", ["Salt Lake City", "Orem", "Provo"]),
             ("Oregon", ["Portland", "Eugene"]),
             ("Arizona", ["Phoenix", "Tucson", "Mesa"])],
    "East": [("New York", ["New York City", "Buffalo", "Rochester", "Albany"]),
             ("Pennsylvania", ["Philadelphia", "Pittsburgh", "Allentown"]),
             ("Massachusetts", ["Boston", "Cambridge", "Worcester"]),
             ("New Jersey", ["Newark", "Jersey City", "Paterson"]),
             ("Ohio", ["Columbus", "Cleveland", "Cincinnati"])],
    "Central": [("Illinois", ["Chicago", "Aurora", "Naperville"]),
                ("Texas", ["Houston", "Dallas", "Austin", "San Antonio", "Fort Worth"]),
                ("Michigan", ["Detroit", "Grand Rapids", "Warren"]),
                ("Wisconsin", ["Milwaukee", "Madison", "Green Bay"]),
                ("Indiana", ["Indianapolis", "Fort Wayne", "Lafayette"])],
    "South": [("Florida", ["Miami", "Fort Lauderdale", "Orlando", "Tampa", "Jacksonville"]),
              ("North Carolina", ["Charlotte", "Raleigh", "Greensboro"]),
              ("Georgia", ["Atlanta", "Columbus", "Savannah"]),
              ("Tennessee", ["Nashville", "Memphis", "Knoxville"]),
              ("Virginia", ["Richmond", "Virginia Beach", "Norfolk"]),
              ("Kentucky", ["Louisville", "Lexington", "Henderson"])]
}

customers = [
    ("Claire Gute", "Consumer"), ("Darrin Van Huff", "Corporate"), ("Sean O'Donnell", "Consumer"),
    ("Brosina Hoffman", "Consumer"), ("Andrew Allen", "Consumer"), ("Irene Maddox", "Consumer"),
    ("Harold Pawlan", "Home Office"), ("Pete Kriz", "Consumer"), ("Alejandro Grove", "Consumer"),
    ("Zuschuss Donatelli", "Consumer"), ("Ken Black", "Corporate"), ("Sandra Flanagan", "Consumer"),
    ("Emily Phan", "Consumer"), ("Eric Hoffmann", "Consumer"), ("Tracy Blumstein", "Consumer"),
    ("Matt Abelman", "Home Office"), ("Gene Hale", "Corporate"), ("Steve Nguyen", "Home Office"),
    ("Linda Cazamias", "Corporate"), ("Ruben Dartt", "Consumer"), ("Erin Smith", "Corporate"),
    ("Odella Nelson", "Corporate"), ("Patrick O'Donnell", "Consumer"), ("Lena Creighton", "Consumer"),
    ("Valerie Mitchum", "Home Office"), ("Mick Brown", "Consumer"), ("Anthony Jacobs", "Corporate"),
    ("Pauline Chand", "Consumer"), ("Delfina Latchford", "Consumer"), ("Barry Pond", "Corporate"),
    ("Roy Skaria", "Corporate"), ("Carlos Soltero", "Consumer"), ("Chuck Clark", "Home Office"),
    ("Bill Stewart", "Corporate"), ("Kelly Lampkin", "Corporate"), ("Sanjit Chand", "Consumer"),
    ("Denny Ward", "Consumer"), ("Arthur Prichep", "Consumer"), ("Harry Marie", "Corporate"),
    ("Sonia Cooley", "Consumer"), ("Dan Lawera", "Consumer"), ("Raymond Buch", "Consumer"),
    ("Zuschuss Carroll", "Consumer"), ("Ken Lonsdale", "Corporate"), ("Hunter Lopez", "Consumer"),
    ("Tamara Chand", "Corporate"), ("Sanjit Engle", "Consumer"), ("Maria Etezadi", "Home Office"),
    ("Justin Deggeller", "Corporate"), ("Tom Prescott", "Consumer"), ("Craig Carreira", "Consumer")
]

start_date = datetime(2021, 1, 1)
end_date = datetime(2024, 12, 31)
total_days = (end_date - start_date).days

dataset = []
order_counter = 1000

for i in range(1200):
    # Skew dates slightly towards Q4 each year
    day_offset = random.randint(0, total_days)
    order_dt = start_date + timedelta(days=day_offset)
    # Seasonal boost in Nov-Dec
    if random.random() < 0.25:
        q4_year = random.choice([2021, 2022, 2023, 2024])
        order_dt = datetime(q4_year, random.choice([11, 12]), random.randint(1, 28))

    ship_dt = order_dt + timedelta(days=random.randint(2, 6))
    order_id = f"CA-{order_dt.year}-{order_counter + (i // 2)}"

    cust_name, cust_seg = random.choice(customers)
    # 70% keep segment, 30% random
    if random.random() < 0.2:
        cust_seg = random.choice(["Consumer", "Corporate", "Home Office"])

    region = random.choice(["West", "East", "Central", "South"])
    state_info = random.choice(regions_states[region])
    state_name = state_info[0]
    city_name = random.choice(state_info[1])

    cat = random.choice(["Furniture", "Office Supplies", "Technology"])
    subcat = random.choice(subcategories[cat])
    prod_name = random.choice(sample_products[subcat])

    qty = random.randint(1, 9)

    # Base price range per subcategory
    if cat == "Technology":
        if subcat == "Copiers":
            base_unit_price = random.uniform(800, 2500)
            base_margin = random.uniform(0.35, 0.50)
            discount = random.choice([0.0, 0.0, 0.0, 0.1, 0.2])
        elif subcat == "Phones":
            base_unit_price = random.uniform(250, 950)
            base_margin = random.uniform(0.20, 0.35)
            discount = random.choice([0.0, 0.0, 0.1, 0.2])
        elif subcat == "Machines":
            base_unit_price = random.uniform(300, 1500)
            base_margin = random.uniform(0.15, 0.30)
            discount = random.choice([0.0, 0.1, 0.2, 0.4])
        else: # Accessories
            base_unit_price = random.uniform(35, 250)
            base_margin = random.uniform(0.25, 0.40)
            discount = random.choice([0.0, 0.0, 0.1, 0.2])
    elif cat == "Furniture":
        if subcat == "Tables":
            base_unit_price = random.uniform(200, 900)
            base_margin = random.uniform(0.05, 0.15)
            # Tables often heavily discounted in Superstore!
            discount = random.choice([0.2, 0.3, 0.4, 0.45, 0.5, 0.6])
        elif subcat == "Chairs":
            base_unit_price = random.uniform(150, 850)
            base_margin = random.uniform(0.18, 0.32)
            discount = random.choice([0.0, 0.1, 0.2, 0.3])
        elif subcat == "Bookcases":
            base_unit_price = random.uniform(100, 450)
            base_margin = random.uniform(0.12, 0.25)
            discount = random.choice([0.0, 0.15, 0.2, 0.35])
        else: # Furnishings
            base_unit_price = random.uniform(20, 120)
            base_margin = random.uniform(0.20, 0.38)
            discount = random.choice([0.0, 0.0, 0.1, 0.2])
    else: # Office Supplies
        if subcat == "Binders":
            base_unit_price = random.uniform(8, 120)
            base_margin = random.uniform(0.25, 0.45)
            # Central region has crazy binder discounts in Kaggle superstore (0.8!)
            if region == "Central" and random.random() < 0.45:
                discount = 0.8
            else:
                discount = random.choice([0.0, 0.0, 0.1, 0.2, 0.7])
        elif subcat == "Storage":
            base_unit_price = random.uniform(40, 350)
            base_margin = random.uniform(0.20, 0.32)
            discount = random.choice([0.0, 0.0, 0.1, 0.2])
        elif subcat == "Appliances":
            base_unit_price = random.uniform(80, 450)
            base_margin = random.uniform(0.22, 0.35)
            discount = random.choice([0.0, 0.1, 0.2, 0.3])
        else:
            base_unit_price = random.uniform(5, 60)
            base_margin = random.uniform(0.28, 0.48)
            discount = random.choice([0.0, 0.0, 0.0, 0.1, 0.2])

    undiscounted_sales = base_unit_price * qty
    sales = round(undiscounted_sales * (1.0 - discount), 2)
    cogs = undiscounted_sales * (1.0 - base_margin)
    profit = round(sales - cogs, 2)

    row = {
        "Row ID": i + 1,
        "Order ID": order_id,
        "Order Date": order_dt.strftime("%Y-%m-%d"),
        "Ship Date": ship_dt.strftime("%Y-%m-%d"),
        "Customer Name": cust_name,
        "Segment": cust_seg,
        "Country": "United States",
        "City": city_name,
        "State": state_name,
        "Postal Code": f"{random.randint(10000, 99999)}",
        "Region": region,
        "Category": cat,
        "Sub-Category": subcat,
        "Product Name": prod_name,
        "Sales": sales,
        "Quantity": qty,
        "Discount": round(discount, 2),
        "Profit": profit
    }
    dataset.append(row)

# Sort by order date
dataset.sort(key=lambda x: x["Order Date"])

# Generate CSV file
csv_lines = [",".join([f'"{k}"' for k in dataset[0].keys()])]
for row in dataset:
    line = []
    for k, v in row.items():
        if isinstance(v, str):
            line.append(f'"{v}"')
        else:
            line.append(str(v))
    csv_lines.append(",".join(line))

csv_content = "\n".join(csv_lines)
csv_path = "/Users/aditijhinjar/.gemini/antigravity-ide/scratch/insightview/superstore_sample.csv"
with open(csv_path, "w", encoding="utf-8") as f:
    f.write(csv_content)

print(f"Generated {len(dataset)} sample rows into {csv_path}")

# Pick first 150 rows as initial demo data JSON embedded in HTML
demo_json = json.dumps(dataset[:160], indent=2)
with open("/Users/aditijhinjar/.gemini/antigravity-ide/scratch/insightview/embedded_demo.json", "w") as f:
    f.write(demo_json)
