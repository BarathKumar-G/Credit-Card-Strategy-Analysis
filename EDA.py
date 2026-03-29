import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# ── PATHS ──────────────────────────────────────────────────────────────────────
DIM_CUSTOMER_PATH = "dim_customers.csv"
FACT_SALES_PATH   = "fact_spends.csv"

plt.rcParams.update({
    "figure.facecolor": "#0e1117",
    "axes.facecolor":   "#1a1d27",
    "axes.edgecolor":   "#2e3250",
    "axes.labelcolor":  "#c2c0b6",
    "xtick.color":      "#888780",
    "ytick.color":      "#888780",
    "text.color":       "#c2c0b6",
    "grid.color":       "#2e3250",
    "grid.linestyle":   "--",
    "grid.alpha":       0.5,
    "font.family":      "sans-serif",
    "font.size":        11,
})
PALETTE = ["#7F77DD","#1D9E75","#EF9F27","#D85A30","#378ADD",
           "#639922","#D4537E","#BA7517","#E24B4A","#888780"]

def save(name):
    plt.tight_layout()
    plt.savefig(f"{name}.png", dpi=150, bbox_inches="tight")
    plt.show()
    print(f"Saved: {name}.png")

# ══════════════════════════════════════════════════════════════════════════════
# LOAD
# ══════════════════════════════════════════════════════════════════════════════
dim  = pd.read_csv(DIM_CUSTOMER_PATH)
fact = pd.read_csv(FACT_SALES_PATH)

dim.columns  = dim.columns.str.strip().str.replace(" ", "_").str.lower()
fact.columns = fact.columns.str.strip().str.replace(" ", "_").str.lower()

if "payment_t" in fact.columns:
    fact.rename(columns={"payment_t": "payment_type"}, inplace=True)

# ══════════════════════════════════════════════════════════════════════════════
# 1. SHAPE & DTYPES
# ══════════════════════════════════════════════════════════════════════════════
print("=" * 60)
print("  MITRON BANK — EDA (Dataset Description)")
print("=" * 60)

print("\n── dim_customer")
print(f"   Rows    : {dim.shape[0]:,}")
print(f"   Columns : {dim.shape[1]}")
print(dim.dtypes.to_string())

print("\n── fact_sales")
print(f"   Rows    : {fact.shape[0]:,}")
print(f"   Columns : {fact.shape[1]}")
print(fact.dtypes.to_string())

# ══════════════════════════════════════════════════════════════════════════════
# 2. SAMPLE ROWS
# ══════════════════════════════════════════════════════════════════════════════
print("\n── dim_customer — first 5 rows:")
print(dim.head().to_string())

print("\n── fact_sales — first 5 rows:")
print(fact.head().to_string())

# ══════════════════════════════════════════════════════════════════════════════
# 3. MISSING VALUES
# ══════════════════════════════════════════════════════════════════════════════
print("\n── Missing Values — dim_customer:")
print(dim.isnull().sum().to_string())

print("\n── Missing Values — fact_sales:")
print(fact.isnull().sum().to_string())

# ══════════════════════════════════════════════════════════════════════════════
# 4. DUPLICATES & RELATIONSHIP CHECK
# ══════════════════════════════════════════════════════════════════════════════
print("\n── Duplicate customer_ids in dim_customer :",
      dim["customer_id"].duplicated().sum())
print("── Orphan transactions (no matching customer):",
      fact[~fact["customer_id"].isin(dim["customer_id"])].shape[0])

# ══════════════════════════════════════════════════════════════════════════════
# 5. UNIQUE VALUES PER COLUMN
# ══════════════════════════════════════════════════════════════════════════════
print("\n── Unique values — dim_customer:")
for col in dim.columns:
    print(f"   {col:<20}: {dim[col].nunique()} unique  "
          f"→  {sorted(dim[col].dropna().unique())[:8]}")

print("\n── Unique values — fact_sales:")
for col in fact.columns:
    print(f"   {col:<20}: {fact[col].nunique()} unique  "
          f"→  {sorted(fact[col].dropna().unique())[:8]}")

# ══════════════════════════════════════════════════════════════════════════════
# 6. DESCRIPTIVE STATISTICS
# ══════════════════════════════════════════════════════════════════════════════
print("\n── Descriptive Stats — dim_customer:")
print(dim.describe().to_string())

print("\n── Descriptive Stats — fact_sales:")
print(fact.describe().to_string())

# ══════════════════════════════════════════════════════════════════════════════
# 7. DISTRIBUTION PLOTS
# ══════════════════════════════════════════════════════════════════════════════

# Plot 1 — dim_customer columns
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
fig.suptitle("dim_customer — Column Distributions", fontsize=14, fontweight="bold")

for i, col in enumerate(["age_group", "city", "occupation", "gender", "marital_status"]):
    ax = axes[i // 3][i % 3]
    vc = dim[col].value_counts()
    ax.bar(vc.index, vc.values, color=PALETTE[:len(vc)], width=0.5)
    ax.set_title(col)
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", rotation=30)
    ax.yaxis.grid(True); ax.set_axisbelow(True)

# avg_income histogram
axes[1][2].hist(dim["avg_income"], bins=30, color=PALETTE[0], edgecolor="#0e1117")
axes[1][2].set_title("avg_income distribution")
axes[1][2].set_xlabel("Income (₹)"); axes[1][2].set_ylabel("Count")
axes[1][2].yaxis.grid(True); axes[1][2].set_axisbelow(True)

save("eda_plot1_dim_customer")

# Plot 2 — fact_sales columns
month_order = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]
fact["month"] = pd.Categorical(fact["month"], categories=month_order, ordered=True)

fig, axes = plt.subplots(1, 4, figsize=(20, 5))
fig.suptitle("fact_sales — Column Distributions", fontsize=14, fontweight="bold")

for i, col in enumerate(["month", "category", "payment_type"]):
    vc = fact[col].value_counts().sort_index() if col == "month" \
         else fact[col].value_counts()
    axes[i].bar(vc.index, vc.values, color=PALETTE[:len(vc)], width=0.5)
    axes[i].set_title(f"{col}")
    axes[i].set_ylabel("Transaction Count")
    axes[i].tick_params(axis="x", rotation=40)
    axes[i].yaxis.grid(True); axes[i].set_axisbelow(True)

axes[3].hist(fact["spend"], bins=40, color=PALETTE[1], edgecolor="#0e1117")
axes[3].set_title("spend distribution")
axes[3].set_xlabel("Spend (₹)"); axes[3].set_ylabel("Count")
axes[3].yaxis.grid(True); axes[3].set_axisbelow(True)

save("eda_plot2_fact_sales")

print("\nEDA complete — dataset described. Analysis is in separate files.")