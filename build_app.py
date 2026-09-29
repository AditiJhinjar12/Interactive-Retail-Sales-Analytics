import json

with open("/Users/aditijhinjar/.gemini/antigravity-ide/scratch/insightview/embedded_demo.json", "r") as f:
    embedded_data_json = f.read()

html_content = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>InsightView — Kaggle Superstore Sales & Profitability Dashboard</title>
  <meta name="description" content="Interactive retail sales & profitability intelligence dashboard for the Kaggle Superstore dataset. Built with dynamic filtering, real-time KPI tracking, and automated strategic insights.">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Lucide Icons -->
  <script src="https://cdn.jsdelivr.net/npm/lucide@0.344.0/dist/umd/lucide.min.js"></script>
  
  <!-- Chart.js 4.4 -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  
  <!-- PapaParse for Browser CSV Parsing -->
  <script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>
  
  <!-- Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

  <style>
    /* ==========================================================================
       CSS VARIABLES & THEMES
       ========================================================================== */
    :root {{
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-xl: 20px;
      --radius-full: 9999px;
      --transition-smooth: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    /* DARK THEME (DEFAULT) */
    [data-theme="dark"] {{
      --bg-primary: #070B14;
      --bg-secondary: #0D1322;
      --bg-card: rgba(18, 26, 43, 0.85);
      --bg-card-hover: rgba(26, 37, 60, 0.95);
      --bg-glass: rgba(13, 19, 34, 0.7);
      --bg-input: #151F33;
      --border-color: rgba(255, 255, 255, 0.08);
      --border-focus: rgba(6, 182, 212, 0.5);
      --border-subtle: rgba(255, 255, 255, 0.04);
      
      --text-primary: #F8FAFC;
      --text-secondary: #94A3B8;
      --text-muted: #64748B;
      
      --accent-cyan: #06B6D4;
      --accent-cyan-glow: rgba(6, 182, 212, 0.25);
      --accent-emerald: #10B981;
      --accent-emerald-glow: rgba(16, 185, 129, 0.25);
      --accent-rose: #F43F5E;
      --accent-rose-glow: rgba(244, 63, 94, 0.25);
      --accent-indigo: #6366F1;
      --accent-indigo-glow: rgba(99, 102, 241, 0.25);
      --accent-amber: #F59E0B;
      --accent-amber-glow: rgba(245, 158, 11, 0.25);
      --accent-purple: #A855F7;

      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.4);
      --shadow-md: 0 8px 24px -4px rgba(0, 0, 0, 0.5);
      --shadow-lg: 0 16px 36px -6px rgba(0, 0, 0, 0.6);
      --shadow-glow: 0 0 25px rgba(6, 182, 212, 0.15);

      --chart-grid: rgba(255, 255, 255, 0.06);
      --chart-text: #94A3B8;
    }}

    /* LIGHT THEME */
    [data-theme="light"] {{
      --bg-primary: #F4F6FB;
      --bg-secondary: #FFFFFF;
      --bg-card: rgba(255, 255, 255, 0.95);
      --bg-card-hover: #FFFFFF;
      --bg-glass: rgba(255, 255, 255, 0.85);
      --bg-input: #F1F5F9;
      --border-color: rgba(0, 0, 0, 0.08);
      --border-focus: rgba(79, 70, 229, 0.5);
      --border-subtle: rgba(0, 0, 0, 0.04);
      
      --text-primary: #0F172A;
      --text-secondary: #475569;
      --text-muted: #94A3B8;
      
      --accent-cyan: #0284C7;
      --accent-cyan-glow: rgba(2, 132, 199, 0.15);
      --accent-emerald: #059669;
      --accent-emerald-glow: rgba(5, 150, 105, 0.15);
      --accent-rose: #E11D48;
      --accent-rose-glow: rgba(225, 29, 72, 0.15);
      --accent-indigo: #4F46E5;
      --accent-indigo-glow: rgba(79, 70, 229, 0.15);
      --accent-amber: #D97706;
      --accent-amber-glow: rgba(217, 119, 6, 0.15);
      --accent-purple: #9333EA;

      --shadow-sm: 0 2px 6px rgba(0, 0, 0, 0.04);
      --shadow-md: 0 8px 20px rgba(0, 0, 0, 0.06);
      --shadow-lg: 0 16px 32px rgba(0, 0, 0, 0.08);
      --shadow-glow: 0 0 20px rgba(79, 70, 229, 0.08);

      --chart-grid: rgba(0, 0, 0, 0.06);
      --chart-text: #64748B;
    }}

    /* ==========================================================================
       RESET & BASE STYLES
       ========================================================================== */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.5;
      min-height: 100vh;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 10% 15%, rgba(6, 182, 212, 0.07) 0%, transparent 40%),
        radial-gradient(circle at 90% 80%, rgba(99, 102, 241, 0.06) 0%, transparent 40%);
      background-attachment: fixed;
      transition: background-color 0.3s ease, color 0.3s ease;
    }}

    /* Modern Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: var(--bg-primary);
    }}
    ::-webkit-scrollbar-thumb {{
      background: var(--bg-input);
      border-radius: var(--radius-full);
      border: 2px solid var(--bg-primary);
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: var(--text-muted);
    }}

    .app-container {{
      max-width: 1680px;
      margin: 0 auto;
      padding: 20px 24px 60px 24px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}

    /* ==========================================================================
       HEADER & NAVIGATION BAR
       ========================================================================== */
    .app-header {{
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-xl);
      padding: 16px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      box-shadow: var(--shadow-md);
      position: relative;
    }}

    .brand-section {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .brand-logo {{
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, var(--accent-cyan), var(--accent-indigo));
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
      box-shadow: 0 4px 14px var(--accent-cyan-glow);
    }}

    .brand-text h1 {{
      font-size: 1.35rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      background: linear-gradient(120deg, var(--text-primary) 30%, var(--accent-cyan));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .brand-text p {{
      font-size: 0.8rem;
      color: var(--text-secondary);
      font-weight: 500;
    }}

    .data-status-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 0.78rem;
      font-weight: 600;
      transition: var(--transition-smooth);
    }}

    .status-demo {{
      background: rgba(245, 158, 11, 0.12);
      color: var(--accent-amber);
      border: 1px solid rgba(245, 158, 11, 0.3);
      animation: pulse-border 2.5s infinite;
    }}

    .status-live {{
      background: rgba(16, 185, 129, 0.12);
      color: var(--accent-emerald);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}

    .pulse-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: currentColor;
      box-shadow: 0 0 8px currentColor;
    }}

    @keyframes pulse-border {{
      0%, 100% {{ box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.2); }}
      50% {{ box-shadow: 0 0 0 6px rgba(245, 158, 11, 0); }}
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    /* Buttons */
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 9px 16px;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition-smooth);
      border: 1px solid transparent;
      outline: none;
      font-family: var(--font-sans);
      user-select: none;
    }}

    .btn-primary {{
      background: linear-gradient(135deg, var(--accent-cyan), var(--accent-indigo));
      color: #FFFFFF;
      box-shadow: 0 4px 14px var(--accent-cyan-glow);
    }}
    .btn-primary:hover {{
      transform: translateY(-1px);
      box-shadow: 0 6px 20px var(--accent-cyan-glow);
      filter: brightness(1.08);
    }}

    .btn-secondary {{
      background: var(--bg-input);
      color: var(--text-primary);
      border: 1px solid var(--border-color);
    }}
    .btn-secondary:hover {{
      background: var(--bg-card-hover);
      border-color: var(--accent-cyan);
      transform: translateY(-1px);
    }}

    .btn-outline {{
      background: transparent;
      color: var(--text-secondary);
      border: 1px solid var(--border-color);
    }}
    .btn-outline:hover {{
      color: var(--text-primary);
      border-color: var(--text-secondary);
      background: var(--bg-input);
    }}

    .btn-icon {{
      padding: 9px;
      border-radius: var(--radius-md);
      background: var(--bg-input);
      color: var(--text-secondary);
      border: 1px solid var(--border-color);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition-smooth);
    }}
    .btn-icon:hover {{
      color: var(--text-primary);
      border-color: var(--accent-cyan);
      transform: translateY(-1px);
    }}

    /* ==========================================================================
       DRAG & DROP UPLOAD HERO BANNER
       ========================================================================== */
    .upload-zone {{
      background: var(--bg-card);
      border: 2px dashed var(--border-color);
      border-radius: var(--radius-lg);
      padding: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      cursor: pointer;
      transition: var(--transition-smooth);
      position: relative;
      overflow: hidden;
    }}

    .upload-zone:hover, .upload-zone.dragover {{
      border-color: var(--accent-cyan);
      background: var(--bg-card-hover);
      box-shadow: 0 0 25px var(--accent-cyan-glow);
      transform: scale(1.002);
    }}

    .upload-zone-left {{
      display: flex;
      align-items: center;
      gap: 18px;
    }}

    .upload-icon-circle {{
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--accent-cyan);
      flex-shrink: 0;
      transition: var(--transition-smooth);
    }}
    .upload-zone:hover .upload-icon-circle {{
      background: var(--accent-cyan);
      color: #FFFFFF;
      transform: scale(1.08);
    }}

    .upload-text h3 {{
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 2px;
    }}

    .upload-text p {{
      font-size: 0.8rem;
      color: var(--text-secondary);
    }}

    .upload-tags {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .tag-pill {{
      padding: 4px 10px;
      border-radius: var(--radius-full);
      background: var(--bg-input);
      color: var(--text-muted);
      font-size: 0.72rem;
      font-weight: 600;
      border: 1px solid var(--border-subtle);
    }}

    #csvFileInput {{
      display: none;
    }}

    /* ==========================================================================
       FILTERS CONTROL PANEL
       ========================================================================== */
    .filter-panel {{
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 18px 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-shadow: var(--shadow-sm);
    }}

    .filter-header-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }}

    .filter-title {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--text-primary);
    }}

    .filter-active-count {{
      font-size: 0.76rem;
      padding: 3px 9px;
      border-radius: var(--radius-full);
      background: var(--accent-cyan-glow);
      color: var(--accent-cyan);
      font-weight: 600;
    }}

    .filter-controls-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 14px;
      align-items: end;
    }}

    .filter-group {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .filter-group label {{
      font-size: 0.76rem;
      font-weight: 600;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .form-select, .form-input {{
      width: 100%;
      padding: 9px 12px;
      border-radius: var(--radius-md);
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      font-family: var(--font-sans);
      font-size: 0.85rem;
      font-weight: 500;
      outline: none;
      transition: var(--transition-smooth);
    }}

    .form-select:focus, .form-input:focus {{
      border-color: var(--accent-cyan);
      box-shadow: 0 0 0 3px var(--accent-cyan-glow);
    }}

    .date-preset-pills {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }}

    .preset-pill {{
      padding: 5px 11px;
      border-radius: var(--radius-full);
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      font-size: 0.74rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition-smooth);
    }}

    .preset-pill:hover {{
      color: var(--text-primary);
      border-color: var(--accent-cyan);
    }}

    .preset-pill.active {{
      background: var(--accent-cyan);
      color: #FFFFFF;
      border-color: var(--accent-cyan);
      box-shadow: 0 2px 8px var(--accent-cyan-glow);
    }}

    /* ==========================================================================
       6 KPI CARDS GRID
       ========================================================================== */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 16px;
    }}

    .kpi-card {{
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 12px;
      box-shadow: var(--shadow-sm);
      transition: var(--transition-smooth);
      position: relative;
      overflow: hidden;
    }}

    .kpi-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: rgba(255, 255, 255, 0.15);
    }}

    .kpi-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, transparent, var(--kpi-accent, var(--accent-cyan)), transparent);
      opacity: 0.8;
    }}

    .kpi-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .kpi-label {{
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }}

    .kpi-icon-box {{
      width: 36px;
      height: 36px;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--kpi-accent-glow, var(--accent-cyan-glow));
      color: var(--kpi-accent, var(--accent-cyan));
    }}

    .kpi-value-container {{
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .kpi-value {{
      font-family: var(--font-mono);
      font-size: 1.8rem;
      font-weight: 700;
      letter-spacing: -0.03em;
      color: var(--text-primary);
    }}

    .kpi-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.76rem;
      color: var(--text-muted);
      border-top: 1px solid var(--border-subtle);
      padding-top: 8px;
    }}

    .kpi-trend-badge {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      font-size: 0.72rem;
      font-family: var(--font-mono);
    }}

    .trend-up {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-emerald);
    }}

    .trend-down {{
      background: rgba(244, 63, 94, 0.15);
      color: var(--accent-rose);
    }}

    .trend-neutral {{
      background: var(--bg-input);
      color: var(--text-muted);
    }}

    /* ==========================================================================
       4 AUTO-GENERATED STRATEGIC INSIGHTS
       ========================================================================== */
    .insights-section {{
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    .section-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .section-title {{
      font-size: 1.15rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
      color: var(--text-primary);
    }}

    .section-subtitle {{
      font-size: 0.8rem;
      color: var(--text-secondary);
    }}

    .insights-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
    }}

    .insight-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      position: relative;
      transition: var(--transition-smooth);
      box-shadow: var(--shadow-sm);
    }}

    .insight-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: var(--insight-color, var(--accent-cyan));
    }}

    .insight-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }}

    .insight-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      background: var(--insight-bg, var(--accent-cyan-glow));
      color: var(--insight-color, var(--accent-cyan));
    }}

    .insight-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-primary);
      line-height: 1.3;
    }}

    .insight-body {{
      font-size: 0.82rem;
      color: var(--text-secondary);
      line-height: 1.5;
    }}

    .insight-metric-highlight {{
      font-family: var(--font-mono);
      font-weight: 700;
      color: var(--text-primary);
      background: var(--bg-input);
      padding: 1px 6px;
      border-radius: 4px;
      display: inline-block;
    }}

    .insight-action {{
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--insight-color, var(--accent-cyan));
      display: flex;
      align-items: center;
      gap: 6px;
      margin-top: auto;
      padding-top: 6px;
      border-top: 1px dashed var(--border-subtle);
    }}

    /* ==========================================================================
       CHARTS GRID
       ========================================================================== */
    .charts-grid {{
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 20px;
    }}

    .col-span-12 {{ grid-column: span 12; }}
    .col-span-8 {{ grid-column: span 8; }}
    .col-span-6 {{ grid-column: span 6; }}
    .col-span-4 {{ grid-column: span 4; }}

    @media (max-width: 1200px) {{
      .col-span-8, .col-span-4 {{ grid-column: span 12; }}
    }}
    @media (max-width: 900px) {{
      .col-span-6 {{ grid-column: span 12; }}
    }}

    .chart-card {{
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-shadow: var(--shadow-sm);
      position: relative;
    }}

    .chart-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .chart-title-area h3 {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .chart-title-area p {{
      font-size: 0.76rem;
      color: var(--text-secondary);
    }}

    .chart-toggle-group {{
      display: flex;
      background: var(--bg-input);
      padding: 3px;
      border-radius: var(--radius-md);
      gap: 2px;
    }}

    .chart-toggle-btn {{
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--text-secondary);
      background: transparent;
      border: none;
      cursor: pointer;
      transition: var(--transition-smooth);
    }}

    .chart-toggle-btn.active {{
      background: var(--bg-card);
      color: var(--text-primary);
      box-shadow: var(--shadow-sm);
    }}

    .chart-canvas-container {{
      position: relative;
      width: 100%;
      height: 320px;
    }}

    .chart-canvas-container.tall {{
      height: 380px;
    }}

    /* ==========================================================================
       DATA EXPLORER TABLE
       ========================================================================== */
    .table-card {{
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-shadow: var(--shadow-sm);
    }}

    .table-header-controls {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
    }}

    .search-box {{
      position: relative;
      min-width: 280px;
    }}

    .search-box i, .search-box svg {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
      width: 16px;
      height: 16px;
    }}

    .search-box input {{
      padding-left: 36px;
    }}

    .table-wrapper {{
      width: 100%;
      overflow-x: auto;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-subtle);
    }}

    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
      text-align: left;
    }}

    .data-table th {{
      background: var(--bg-input);
      color: var(--text-secondary);
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.72rem;
      letter-spacing: 0.04em;
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-color);
      cursor: pointer;
      user-select: none;
      white-space: nowrap;
    }}

    .data-table th:hover {{
      color: var(--accent-cyan);
    }}

    .data-table td {{
      padding: 11px 14px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-primary);
      white-space: nowrap;
    }}

    .data-table tr:hover td {{
      background: var(--bg-input);
    }}

    .data-table .font-mono {{
      font-family: var(--font-mono);
    }}

    .badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      font-size: 0.72rem;
      font-weight: 600;
    }}

    .badge-profit-pos {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-emerald);
    }}

    .badge-profit-neg {{
      background: rgba(244, 63, 94, 0.15);
      color: var(--accent-rose);
    }}

    .table-pagination {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      font-size: 0.8rem;
      color: var(--text-secondary);
      padding-top: 8px;
    }}

    .pagination-actions {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* ==========================================================================
       MODAL & TOASTS
       ========================================================================== */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 20px;
    }}

    .modal-backdrop.active {{
      display: flex;
    }}

    .modal-content {{
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-xl);
      max-width: 600px;
      width: 100%;
      padding: 26px;
      box-shadow: var(--shadow-lg);
      display: flex;
      flex-direction: column;
      gap: 18px;
      max-height: 90vh;
      overflow-y: auto;
    }}

    .modal-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .toast-container {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9999;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .toast {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-lg);
      border-radius: var(--radius-md);
      padding: 12px 18px;
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.85rem;
      color: var(--text-primary);
      animation: slide-in 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    @keyframes slide-in {{
      from {{ transform: translateY(20px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}

    /* Print styling */
    @media print {{
      body {{ background: #FFF !important; color: #000 !important; }}
      .app-header, .upload-zone, .filter-panel, .header-actions, .table-pagination, .btn {{ display: none !important; }}
      .kpi-card, .chart-card, .insight-card {{ border: 1px solid #CCC !important; box-shadow: none !important; }}
    }}
  </style>
</head>
<body>

  <div class="app-container">
    
    <!-- HEADER BAR -->
    <header class="app-header">
      <div class="brand-section">
        <div class="brand-logo">
          <i data-lucide="bar-chart-3" style="width: 24px; height: 24px;"></i>
        </div>
        <div class="brand-text">
          <h1>InsightView <span style="font-size: 0.72rem; font-weight: 600; padding: 2px 8px; border-radius: var(--radius-full); background: var(--accent-cyan-glow); color: var(--accent-cyan); text-transform: uppercase;">Retail Intelligence</span></h1>
          <p>Kaggle Superstore Analytics & Profitability Engine</p>
        </div>
      </div>

      <!-- Live / Demo Status Badge -->
      <div id="dataStatusBadge" class="data-status-badge status-demo">
        <span class="pulse-dot"></span>
        <span id="dataStatusText">DEMO DATA - not real (160 records)</span>
      </div>

      <!-- Action Buttons -->
      <div class="header-actions">
        <button id="btnLoadCsv" class="btn btn-primary" title="Upload your Kaggle Superstore CSV file">
          <i data-lucide="upload-cloud" style="width: 16px; height: 16px;"></i>
          <span>Load Superstore CSV</span>
        </button>

        <button id="btnDownloadSample" class="btn btn-secondary" title="Download the full 1,200 row sample Superstore CSV">
          <i data-lucide="download" style="width: 16px; height: 16px;"></i>
          <span>Sample CSV</span>
        </button>

        <button id="btnResetDemo" class="btn btn-outline" style="display: none;" title="Revert to initial demo dataset">
          <i data-lucide="rotate-ccw" style="width: 16px; height: 16px;"></i>
          <span>Reset Demo</span>
        </button>

        <button id="btnExportFiltered" class="btn btn-secondary" title="Export currently filtered dataset to CSV">
          <i data-lucide="file-spreadsheet" style="width: 16px; height: 16px;"></i>
          <span>Export CSV</span>
        </button>

        <button id="themeToggleBtn" class="btn-icon" title="Toggle Light/Dark Theme">
          <i id="themeIcon" data-lucide="sun" style="width: 18px; height: 18px;"></i>
        </button>

        <button id="btnDiagnostics" class="btn-icon" title="View Column Mapping & Diagnostics">
          <i data-lucide="sliders" style="width: 18px; height: 18px;"></i>
        </button>
      </div>
    </header>

    <!-- DRAG & DROP UPLOAD HERO ZONE -->
    <div id="dropZone" class="upload-zone">
      <input type="file" id="csvFileInput" accept=".csv, .txt, .tsv, text/csv">
      <div class="upload-zone-left">
        <div class="upload-icon-circle">
          <i data-lucide="file-up" style="width: 26px; height: 26px;"></i>
        </div>
        <div class="upload-text">
          <h3>Drop your Superstore CSV file here, or click to browse</h3>
          <p>Tolerates Latin-1 / Windows-1252 / UTF-8 encoding. Matches columns automatically by header name.</p>
        </div>
      </div>
      <div class="upload-tags">
        <span class="tag-pill">Kaggle vivek468/superstore compatible</span>
        <span class="tag-pill">Client-side Parse</span>
        <span class="tag-pill">Zero Server Upload</span>
      </div>
    </div>

    <!-- FILTER CONTROL PANEL -->
    <section class="filter-panel">
      <div class="filter-header-row">
        <div class="filter-title">
          <i data-lucide="filter" style="width: 16px; height: 16px; color: var(--accent-cyan);"></i>
          <span>Interactive Filter Engine</span>
          <span id="filteredCountBadge" class="filter-active-count">Showing 160 / 160 rows (100%)</span>
        </div>
        <div class="date-preset-pills">
          <button class="preset-pill active" data-preset="all">All Time</button>
          <button class="preset-pill" data-preset="2024">2024</button>
          <button class="preset-pill" data-preset="2023">2023</button>
          <button class="preset-pill" data-preset="2022">2022</button>
          <button class="preset-pill" data-preset="2021">2021</button>
          <button class="preset-pill" data-preset="q4">Q4 Peak Season</button>
          <button id="btnResetFilters" class="btn btn-outline" style="padding: 4px 10px; font-size: 0.72rem;">
            <i data-lucide="refresh-cw" style="width: 12px; height: 12px;"></i>
            <span>Reset All</span>
          </button>
        </div>
      </div>

      <div class="filter-controls-grid">
        <!-- Date Range Pickers -->
        <div class="filter-group">
          <label>Start Date</label>
          <input type="date" id="filterStartDate" class="form-input">
        </div>

        <div class="filter-group">
          <label>End Date</label>
          <input type="date" id="filterEndDate" class="form-input">
        </div>

        <!-- Region Filter -->
        <div class="filter-group">
          <label>Region</label>
          <select id="filterRegion" class="form-select">
            <option value="ALL">All Regions (West, East, Central, South)</option>
            <option value="West">West</option>
            <option value="East">East</option>
            <option value="Central">Central</option>
            <option value="South">South</option>
          </select>
        </div>

        <!-- Category Filter -->
        <div class="filter-group">
          <label>Category</label>
          <select id="filterCategory" class="form-select">
            <option value="ALL">All Categories</option>
            <option value="Furniture">Furniture</option>
            <option value="Office Supplies">Office Supplies</option>
            <option value="Technology">Technology</option>
          </select>
        </div>

        <!-- Customer Segment Filter -->
        <div class="filter-group">
          <label>Customer Segment</label>
          <select id="filterSegment" class="form-select">
            <option value="ALL">All Segments</option>
            <option value="Consumer">Consumer</option>
            <option value="Corporate">Corporate</option>
            <option value="Home Office">Home Office</option>
          </select>
        </div>

        <!-- Profitability Filter -->
        <div class="filter-group">
          <label>Profitability</label>
          <select id="filterProfitability" class="form-select">
            <option value="ALL">All Transactions</option>
            <option value="PROFIT">Profitable Orders Only (Profit > $0)</option>
            <option value="LOSS">Loss-Making Orders (Profit < $0)</option>
          </select>
        </div>
      </div>
    </section>

    <!-- 6 KPI CARDS -->
    <section class="kpi-grid">
      <!-- 1. Total Sales -->
      <div class="kpi-card" style="--kpi-accent: var(--accent-cyan); --kpi-accent-glow: var(--accent-cyan-glow);">
        <div class="kpi-header">
          <span class="kpi-label">Total Sales</span>
          <div class="kpi-icon-box">
            <i data-lucide="dollar-sign" style="width: 20px; height: 20px;"></i>
          </div>
        </div>
        <div class="kpi-value-container">
          <span id="kpiSales" class="kpi-value">$0</span>
        </div>
        <div class="kpi-footer">
          <span>Gross Revenue</span>
          <span id="kpiSalesYoY" class="kpi-trend-badge trend-up">+0.0% YoY</span>
        </div>
      </div>

      <!-- 2. Total Profit -->
      <div class="kpi-card" style="--kpi-accent: var(--accent-emerald); --kpi-accent-glow: var(--accent-emerald-glow);">
        <div class="kpi-header">
          <span class="kpi-label">Total Profit</span>
          <div class="kpi-icon-box">
            <i data-lucide="trending-up" style="width: 20px; height: 20px;"></i>
          </div>
        </div>
        <div class="kpi-value-container">
          <span id="kpiProfit" class="kpi-value">$0</span>
        </div>
        <div class="kpi-footer">
          <span>Net Earnings</span>
          <span id="kpiProfitStatus" class="kpi-trend-badge trend-up">Profitable</span>
        </div>
      </div>

      <!-- 3. Profit Margin % -->
      <div class="kpi-card" style="--kpi-accent: var(--accent-indigo); --kpi-accent-glow: var(--accent-indigo-glow);">
        <div class="kpi-header">
          <span class="kpi-label">Profit Margin</span>
          <div class="kpi-icon-box">
            <i data-lucide="percent" style="width: 20px; height: 20px;"></i>
          </div>
        </div>
        <div class="kpi-value-container">
          <span id="kpiMargin" class="kpi-value">0.0%</span>
        </div>
        <div class="kpi-footer">
          <span>Profit / Sales</span>
          <span id="kpiMarginHealth" class="kpi-trend-badge trend-up">Healthy</span>
        </div>
      </div>

      <!-- 4. Total Orders -->
      <div class="kpi-card" style="--kpi-accent: var(--accent-amber); --kpi-accent-glow: var(--accent-amber-glow);">
        <div class="kpi-header">
          <span class="kpi-label">Total Orders</span>
          <div class="kpi-icon-box">
            <i data-lucide="shopping-bag" style="width: 20px; height: 20px;"></i>
          </div>
        </div>
        <div class="kpi-value-container">
          <span id="kpiOrders" class="kpi-value">0</span>
        </div>
        <div class="kpi-footer">
          <span id="kpiLineItems">0 line items</span>
          <span id="kpiAvgItems" class="kpi-trend-badge trend-neutral">0 items/order</span>
        </div>
      </div>

      <!-- 5. Average Order Value (AOV) -->
      <div class="kpi-card" style="--kpi-accent: var(--accent-purple); --kpi-accent-glow: rgba(168, 85, 247, 0.25);">
        <div class="kpi-header">
          <span class="kpi-label">Avg Order Value (AOV)</span>
          <div class="kpi-icon-box">
            <i data-lucide="receipt" style="width: 20px; height: 20px;"></i>
          </div>
        </div>
        <div class="kpi-value-container">
          <span id="kpiAOV" class="kpi-value">$0.00</span>
        </div>
        <div class="kpi-footer">
          <span>Sales per Order</span>
          <span id="kpiProfitPerOrder" class="kpi-trend-badge trend-neutral">$0.00 profit/ord</span>
        </div>
      </div>

      <!-- 6. YoY Growth -->
      <div class="kpi-card" style="--kpi-accent: var(--accent-rose); --kpi-accent-glow: var(--accent-rose-glow);">
        <div class="kpi-header">
          <span class="kpi-label">YoY Growth</span>
          <div class="kpi-icon-box">
            <i data-lucide="activity" style="width: 20px; height: 20px;"></i>
          </div>
        </div>
        <div class="kpi-value-container">
          <span id="kpiYoY" class="kpi-value">+0.0%</span>
        </div>
        <div class="kpi-footer">
          <span>Latest vs Prior Period</span>
          <span id="kpiYoYBenchmark" class="kpi-trend-badge trend-up">Expanding</span>
        </div>
      </div>
    </section>

    <!-- 4 DYNAMIC AUTO-GENERATED STRATEGIC INSIGHTS -->
    <section class="insights-section">
      <div class="section-header">
        <div>
          <h2 class="section-title">
            <i data-lucide="sparkles" style="width: 20px; height: 20px; color: var(--accent-amber);"></i>
            <span>Automated Strategic Insights</span>
          </h2>
          <p class="section-subtitle">Real-time analytical findings computed from the currently loaded & filtered dataset</p>
        </div>
      </div>

      <div class="insights-grid">
        <!-- Insight 1: Profitability Leakage & Losses -->
        <div class="insight-card" style="--insight-color: var(--accent-rose); --insight-bg: var(--accent-rose-glow);">
          <div class="insight-header">
            <span class="insight-badge">
              <i data-lucide="alert-triangle" style="width: 14px; height: 14px;"></i>
              <span>Profit Leakage Alert</span>
            </span>
          </div>
          <h3 id="insight1Title" class="insight-title">Sub-Category Margin Alert</h3>
          <p id="insight1Body" class="insight-body">Analyzing loss-making sub-categories...</p>
          <div id="insight1Action" class="insight-action">
            <i data-lucide="arrow-right-circle" style="width: 14px; height: 14px;"></i>
            <span>Recommendation: Cap discount limit</span>
          </div>
        </div>

        <!-- Insight 2: Discount Threshold Cliff -->
        <div class="insight-card" style="--insight-color: var(--accent-amber); --insight-bg: var(--accent-amber-glow);">
          <div class="insight-header">
            <span class="insight-badge">
              <i data-lucide="percent" style="width: 14px; height: 14px;"></i>
              <span>Discount Impact Analysis</span>
            </span>
          </div>
          <h3 id="insight2Title" class="insight-title">Discount Cliff at 20%+</h3>
          <p id="insight2Body" class="insight-body">Calculating discount tier impact on margins...</p>
          <div id="insight2Action" class="insight-action">
            <i data-lucide="arrow-right-circle" style="width: 14px; height: 14px;"></i>
            <span>Sweet Spot: Maintain discounts ≤ 15%</span>
          </div>
        </div>

        <!-- Insight 3: Regional Growth & Margin Spread -->
        <div class="insight-card" style="--insight-color: var(--accent-emerald); --insight-bg: var(--accent-emerald-glow);">
          <div class="insight-header">
            <span class="insight-badge">
              <i data-lucide="map-pin" style="width: 14px; height: 14px;"></i>
              <span>Regional Performance</span>
            </span>
          </div>
          <h3 id="insight3Title" class="insight-title">Top Regional Driver</h3>
          <p id="insight3Body" class="insight-body">Evaluating sales & profit distribution by region...</p>
          <div id="insight3Action" class="insight-action">
            <i data-lucide="arrow-right-circle" style="width: 14px; height: 14px;"></i>
            <span>Strategy: Replicate top region pricing</span>
          </div>
        </div>

        <!-- Insight 4: Customer Segment & Seasonality -->
        <div class="insight-card" style="--insight-color: var(--accent-cyan); --insight-bg: var(--accent-cyan-glow);">
          <div class="insight-header">
            <span class="insight-badge">
              <i data-lucide="users" style="width: 14px; height: 14px;"></i>
              <span>Segment & Seasonality</span>
            </span>
          </div>
          <h3 id="insight4Title" class="insight-title">Primary Revenue Driver</h3>
          <p id="insight4Body" class="insight-body">Analyzing customer segments and monthly velocity...</p>
          <div id="insight4Action" class="insight-action">
            <i data-lucide="arrow-right-circle" style="width: 14px; height: 14px;"></i>
            <span>Focus: Maximize Q4 promotional campaigns</span>
          </div>
        </div>
      </div>
    </section>

    <!-- CHARTS GRID -->
    <section class="charts-grid">
      
      <!-- Chart 1: Monthly Sales & Profit Trend (Span 8) -->
      <div class="chart-card col-span-8">
        <div class="chart-header">
          <div class="chart-title-area">
            <h3><i data-lucide="trending-up" style="width: 18px; height: 18px; color: var(--accent-cyan);"></i> Monthly Revenue & Profit Dynamics</h3>
            <p>Time series trajectory showing historical revenue expansion and net profitability</p>
          </div>
          <div class="chart-toggle-group">
            <button class="chart-toggle-btn active" data-chart-view="both" onclick="setMonthlyView('both')">Sales & Profit</button>
            <button class="chart-toggle-btn" data-chart-view="sales" onclick="setMonthlyView('sales')">Sales Only</button>
            <button class="chart-toggle-btn" data-chart-view="profit" onclick="setMonthlyView('profit')">Profit Only</button>
          </div>
        </div>
        <div class="chart-canvas-container">
          <canvas id="monthlyTrendChart"></canvas>
        </div>
      </div>

      <!-- Chart 2: Customer Segment Share (Span 4) -->
      <div class="chart-card col-span-4">
        <div class="chart-header">
          <div class="chart-title-area">
            <h3><i data-lucide="pie-chart" style="width: 18px; height: 18px; color: var(--accent-purple);"></i> Sales & Profit by Segment</h3>
            <p>Consumer vs Corporate vs Home Office revenue & margin</p>
          </div>
        </div>
        <div class="chart-canvas-container">
          <canvas id="segmentDonutChart"></canvas>
        </div>
      </div>

      <!-- Chart 3: Sales & Profit by Category (Span 6) -->
      <div class="chart-card col-span-6">
        <div class="chart-header">
          <div class="chart-title-area">
            <h3><i data-lucide="layers" style="width: 18px; height: 18px; color: var(--accent-indigo);"></i> Sales & Profit by Category</h3>
            <p>Comparison across Furniture, Office Supplies, and Technology</p>
          </div>
          <div class="chart-toggle-group">
            <button id="btnCatViewMain" class="chart-toggle-btn active" onclick="toggleCategoryDrilldown(false)">Main Categories</button>
            <button id="btnCatViewSub" class="chart-toggle-btn" onclick="toggleCategoryDrilldown(true)">Sub-Categories</button>
          </div>
        </div>
        <div class="chart-canvas-container tall">
          <canvas id="categoryBarChart"></canvas>
        </div>
      </div>

      <!-- Chart 4: Sales & Profit by Region (Span 6) -->
      <div class="chart-card col-span-6">
        <div class="chart-header">
          <div class="chart-title-area">
            <h3><i data-lucide="compass" style="width: 18px; height: 18px; color: var(--accent-emerald);"></i> Sales & Profit by Region</h3>
            <p>Geographical breakdown across West, East, Central, and South territories</p>
          </div>
        </div>
        <div class="chart-canvas-container tall">
          <canvas id="regionBarChart"></canvas>
        </div>
      </div>

      <!-- Chart 5: Discount vs. Profit Curve (Span 6) -->
      <div class="chart-card col-span-6">
        <div class="chart-header">
          <div class="chart-title-area">
            <h3><i data-lucide="target" style="width: 18px; height: 18px; color: var(--accent-rose);"></i> Discount vs. Profitability Danger Curve</h3>
            <p>Average Profit Margin % across discount levels (shows the margin decay tipping point)</p>
          </div>
        </div>
        <div class="chart-canvas-container">
          <canvas id="discountProfitChart"></canvas>
        </div>
      </div>

      <!-- Chart 6: Top 10 Products by Performance (Span 6) -->
      <div class="chart-card col-span-6">
        <div class="chart-header">
          <div class="chart-title-area">
            <h3><i data-lucide="award" style="width: 18px; height: 18px; color: var(--accent-amber);"></i> Top 10 Products Ranking</h3>
            <p>Ranked product performers by revenue and net profit</p>
          </div>
          <div class="chart-toggle-group">
            <button id="btnTopSales" class="chart-toggle-btn active" onclick="setProductRankingMode('sales')">Top Sales</button>
            <button id="btnTopProfit" class="chart-toggle-btn" onclick="setProductRankingMode('profit')">Top Profit</button>
            <button id="btnTopLoss" class="chart-toggle-btn" onclick="setProductRankingMode('loss')">Loss-Makers</button>
          </div>
        </div>
        <div class="chart-canvas-container">
          <canvas id="topProductsChart"></canvas>
        </div>
      </div>

    </section>

    <!-- DATA EXPLORER TABLE -->
    <section class="table-card">
      <div class="table-header-controls">
        <div class="chart-title-area">
          <h3><i data-lucide="database" style="width: 18px; height: 18px; color: var(--accent-cyan);"></i> Dataset Explorer & Transaction Inspector</h3>
          <p>Search, filter, and inspect individual transaction lines</p>
        </div>

        <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
          <div class="search-box">
            <i data-lucide="search"></i>
            <input type="text" id="tableSearchInput" class="form-input" placeholder="Search product, customer, city, ID...">
          </div>

          <select id="tablePageSize" class="form-select" style="width: 110px;">
            <option value="10">10 / page</option>
            <option value="25" selected>25 / page</option>
            <option value="50">50 / page</option>
            <option value="100">100 / page</option>
          </select>
        </div>
      </div>

      <div class="table-wrapper">
        <table class="data-table">
          <thead>
            <tr>
              <th onclick="sortTable('orderDate')">Date <i data-lucide="chevrons-up-down" style="width: 12px; height: 12px; display: inline;"></i></th>
              <th onclick="sortTable('orderId')">Order ID</th>
              <th onclick="sortTable('customerName')">Customer</th>
              <th onclick="sortTable('region')">Region / State</th>
              <th onclick="sortTable('category')">Category</th>
              <th onclick="sortTable('productName')">Product Name</th>
              <th onclick="sortTable('sales')" style="text-align: right;">Sales</th>
              <th onclick="sortTable('quantity')" style="text-align: right;">Qty</th>
              <th onclick="sortTable('discount')" style="text-align: right;">Discount</th>
              <th onclick="sortTable('profit')" style="text-align: right;">Profit</th>
              <th onclick="sortTable('profitMargin')" style="text-align: right;">Margin %</th>
            </tr>
          </thead>
          <tbody id="tableBody">
            <!-- Populated via JavaScript -->
          </tbody>
        </table>
      </div>

      <div class="table-pagination">
        <span id="tablePaginationInfo">Showing 1 to 25 of 160 entries</span>
        <div class="pagination-actions">
          <button id="btnPrevPage" class="btn btn-secondary" style="padding: 6px 12px;">Previous</button>
          <span id="tablePageNumber" style="font-weight: 700; padding: 0 8px; font-family: var(--font-mono);">1 / 7</span>
          <button id="btnNextPage" class="btn btn-secondary" style="padding: 6px 12px;">Next</button>
        </div>
      </div>
    </section>

  </div>

  <!-- DIAGNOSTICS & COLUMN MAPPING MODAL -->
  <div id="diagnosticsModal" class="modal-backdrop">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="font-size: 1.1rem; font-weight: 700; display: flex; align-items: center; gap: 8px;">
          <i data-lucide="sliders" style="width: 20px; height: 20px; color: var(--accent-cyan);"></i>
          <span>Dataset Schema & Diagnostics</span>
        </h3>
        <button id="btnCloseModal" class="btn-icon" style="border: none; background: transparent;">
          <i data-lucide="x" style="width: 20px; height: 20px;"></i>
        </button>
      </div>
      <div id="modalBody" style="display: flex; flex-direction: column; gap: 14px; font-size: 0.85rem;">
        <!-- Filled by JS -->
      </div>
    </div>
  </div>

  <!-- TOAST NOTIFICATIONS -->
  <div id="toastContainer" class="toast-container"></div>

  <!-- JAVASCRIPT APPLICATION CODE -->
  <script>
    /* ==========================================================================
       INITIAL DEMO DATASET
       ========================================================================== */
    const INITIAL_DEMO_DATA = {embedded_data_json};

    /* State Variables */
    let rawDataset = [];
    let isLiveDataset = false;
    let loadedFileName = '';
    let detectedEncoding = 'UTF-8 (Default Demo)';
    let mappedColumns = {{}};

    // Active Filter State
    let activeFilters = {{
      startDate: null,
      endDate: null,
      region: 'ALL',
      category: 'ALL',
      segment: 'ALL',
      profitability: 'ALL',
      searchQuery: ''
    }};

    // Table State
    let tableCurrentPage = 1;
    let tablePageSize = 25;
    let tableSortColumn = 'orderDate';
    let tableSortAsc = false;
    let filteredData = [];

    // Chart View States
    let monthlyChartView = 'both'; // 'both', 'sales', 'profit'
    let categoryDrilldown = false; // false = Main, true = Sub-Category
    let productRankingMode = 'sales'; // 'sales', 'profit', 'loss'

    // Chart Instances
    let chartMonthly = null;
    let chartSegment = null;
    let chartCategory = null;
    let chartRegion = null;
    let chartDiscount = null;
    let chartTopProducts = null;

    /* ==========================================================================
       ROBUST DATA PARSER & COLUMN MAPPER
       ========================================================================== */
    const COLUMN_PATTERNS = {{
      orderDate: [/order.?date/i, /order_date/i, /^date$/i],
      shipDate: [/ship.?date/i, /ship_date/i],
      orderId: [/order.?id/i, /order_id/i, /invoice/i, /trans.*id/i],
      customerName: [/customer.?name/i, /cust.*name/i, /customer/i, /client/i],
      segment: [/segment/i, /cust.*segment/i, /customer_segment/i],
      region: [/region/i, /territory/i, /zone/i, /market/i],
      state: [/state/i, /province/i],
      city: [/city/i, /town/i],
      category: [/^category$/i, /product.?category/i, /dept/i],
      subCategory: [/sub.?category/i, /sub_category/i, /subcategory/i, /sub.?cat/i],
      productName: [/product.?name/i, /item.?name/i, /^product$/i, /^item$/i, /description/i],
      sales: [/sales/i, /revenue/i, /gross.?sales/i, /amount/i, /total/i],
      quantity: [/quantity/i, /qty/i, /units/i, /count/i],
      discount: [/discount/i, /disc/i, /disc_rate/i],
      profit: [/profit/i, /net.?profit/i, /net.?income/i, /margin.?amount/i]
    }};

    function autoMapHeaders(headers) {{
      const mapping = {{}};
      const cleanHeaders = headers.map(h => (h || '').trim().replace(/^\\uFEFF/, '').replace(/["']/g, ''));

      for (const [key, regexList] of Object.entries(COLUMN_PATTERNS)) {{
        for (let i = 0; i < cleanHeaders.length; i++) {{
          const header = cleanHeaders[i];
          if (regexList.some(r => r.test(header))) {{
            mapping[key] = headers[i]; // Store original header key
            break;
          }}
        }}
      }}
      return mapping;
    }}

    function parseNumeric(val, defaultVal = 0) {{
      if (val === null || val === undefined) return defaultVal;
      if (typeof val === 'number') return isNaN(val) ? defaultVal : val;
      let s = String(val).trim();
      if (!s) return defaultVal;

      // Handle ($123.45) negative format
      let isNegative = false;
      if (s.startsWith('(') && s.endsWith(')')) {{
        isNegative = true;
        s = s.substring(1, s.length - 1);
      }}

      // Strip currency signs, commas, percent
      s = s.replace(/[$€£¥,]/g, '').trim();
      let n = parseFloat(s);
      if (isNaN(n)) return defaultVal;
      return isNegative ? -n : n;
    }}

    function parseDateString(dateVal) {{
      if (!dateVal) return '2023-01-01';
      if (dateVal instanceof Date && !isNaN(dateVal.getTime())) {{
        return dateVal.toISOString().split('T')[0];
      }}

      let s = String(dateVal).trim().replace(/["']/g, '');
      if (!s) return '2023-01-01';

      // Excel numeric date (e.g. 44560)
      if (/^\\d{{5}}$/.test(s)) {{
        const excelEpoch = new Date(1899, 11, 30);
        const days = parseInt(s, 10);
        const d = new Date(excelEpoch.getTime() + days * 86400000);
        return d.toISOString().split('T')[0];
      }}

      // YYYY-MM-DD
      if (/^\\d{{4}}-\\d{{1,2}}-\\d{{1,2}}/.test(s)) {{
        const parts = s.split('T')[0].split('-');
        return `${{parts[0]}}-${{parts[1].padStart(2, '0')}}-${{parts[2].padStart(2, '0')}}`;
      }}

      // MM/DD/YYYY or M/D/YY
      if (/^\\d{{1,2}}[\\/\\-]\\d{{1,2}}[\\/\\-]\\d{{2,4}}/.test(s)) {{
        const delimiter = s.includes('/') ? '/' : '-';
        const parts = s.split(delimiter);
        let month = parseInt(parts[0], 10);
        let day = parseInt(parts[1], 10);
        let year = parseInt(parts[2], 10);
        if (year < 100) year += (year < 50 ? 2000 : 1900);
        return `${{year}}-${{String(month).padStart(2, '0')}}-${{String(day).padStart(2, '0')}}`;
      }}

      const parsed = new Date(s);
      if (!isNaN(parsed.getTime())) {{
        return parsed.toISOString().split('T')[0];
      }}

      return '2023-01-01';
    }}

    function transformRawRow(row, mapping, idx) {{
      const getVal = (key, fallback = '') => {{
        const col = mapping[key];
        return (col && row[col] !== undefined && row[col] !== null) ? row[col] : fallback;
      }};

      const orderDate = parseDateString(getVal('orderDate', '2023-01-01'));
      const shipDate = parseDateString(getVal('shipDate', orderDate));
      const sales = parseNumeric(getVal('sales', 0));
      const quantity = Math.max(1, parseInt(getVal('quantity', 1), 10) || 1);
      
      let discount = parseNumeric(getVal('discount', 0));
      if (discount > 1.0 && discount <= 100.0) discount = discount / 100.0; // handle 20 -> 0.20
      discount = Math.min(1.0, Math.max(0.0, discount));

      const profit = parseNumeric(getVal('profit', 0));
      const profitMargin = sales > 0 ? (profit / sales) * 100 : 0;

      return {{
        id: idx + 1,
        orderId: String(getVal('orderId', `ORD-${{idx + 1001}}`)).trim(),
        orderDate: orderDate,
        shipDate: shipDate,
        customerName: String(getVal('customerName', 'Superstore Customer')).trim(),
        segment: String(getVal('segment', 'Consumer')).trim() || 'Consumer',
        region: String(getVal('region', 'West')).trim() || 'West',
        state: String(getVal('state', 'California')).trim() || 'California',
        city: String(getVal('city', 'Los Angeles')).trim() || 'Los Angeles',
        category: String(getVal('category', 'Furniture')).trim() || 'Furniture',
        subCategory: String(getVal('subCategory', 'Chairs')).trim() || 'Chairs',
        productName: String(getVal('productName', 'Commercial Office Supply Item')).trim(),
        sales: Math.round(sales * 100) / 100,
        quantity: quantity,
        discount: Math.round(discount * 100) / 100,
        profit: Math.round(profit * 100) / 100,
        profitMargin: Math.round(profitMargin * 10) / 10
      }};
    }}

    /* ==========================================================================
       FILE UPLOAD & ENCODING TOLERANCE ENGINE
       ========================================================================== */
    async function loadCsvFile(file) {{
      showToast(`Reading ${{file.name}} (${{(file.size / 1024).toFixed(1)}} KB)...`, 'info');
      
      try {{
        const buffer = await file.arrayBuffer();
        let text = '';
        let encodingUsed = 'UTF-8';

        // Attempt UTF-8 decoding first with fatal validation
        try {{
          const utf8Decoder = new TextDecoder('utf-8', {{ fatal: true }});
          text = utf8Decoder.decode(buffer);
          encodingUsed = 'UTF-8';
        }} catch (e) {{
          // Fallback to Latin-1 / Windows-1252
          console.warn('UTF-8 decoding failed, falling back to windows-1252 / Latin-1', e);
          const latinDecoder = new TextDecoder('windows-1252');
          text = latinDecoder.decode(buffer);
          encodingUsed = 'Latin-1 (Windows-1252)';
        }}

        detectedEncoding = encodingUsed;

        // Parse with PapaParse
        Papa.parse(text, {{
          header: true,
          skipEmptyLines: 'greedy',
          dynamicTyping: false,
          complete: function(results) {{
            if (!results.data || results.data.length === 0) {{
              showToast('CSV file is empty or could not be parsed.', 'error');
              return;
            }}

            const headers = results.meta.fields || Object.keys(results.data[0]);
            mappedColumns = autoMapHeaders(headers);

            console.log('Detected Headers:', headers);
            console.log('Mapped Schema:', mappedColumns);

            // Transform rows
            const parsedRows = [];
            for (let i = 0; i < results.data.length; i++) {{
              const row = results.data[i];
              if (Object.keys(row).length <= 1 && !Object.values(row)[0]) continue;
              parsedRows.push(transformRawRow(row, mappedColumns, i));
            }}

            if (parsedRows.length === 0) {{
              showToast('No valid transaction rows found in CSV.', 'error');
              return;
            }}

            // Replace dataset fully
            rawDataset = parsedRows;
            isLiveDataset = true;
            loadedFileName = file.name;

            // Update UI Badges
            updateDatasetStatus(true, `${{file.name}} (${{parsedRows.length.toLocaleString()}} rows)`);
            document.getElementById('btnResetDemo').style.display = 'inline-flex';

            // Reset filters to full span of new data
            resetFilterDatesToDataset();
            applyFilters();

            // Confetti celebration!
            triggerConfetti();
            showToast(`Successfully loaded ${{parsedRows.length.toLocaleString()}} records from ${{file.name}}!`, 'success');
          }},
          error: function(err) {{
            console.error('PapaParse error:', err);
            showToast('Error parsing CSV file: ' + err.message, 'error');
          }}
        }});

      }} catch (err) {{
        console.error('File reading error:', err);
        showToast('Failed to read file: ' + err.message, 'error');
      }}
    }}

    function updateDatasetStatus(isLive, labelText) {{
      const badge = document.getElementById('dataStatusBadge');
      const text = document.getElementById('dataStatusText');
      if (isLive) {{
        badge.className = 'data-status-badge status-live';
        text.textContent = `LIVE DATA: ${{labelText}}`;
      }} else {{
        badge.className = 'data-status-badge status-demo';
        text.textContent = labelText;
      }}
    }}

    function resetFilterDatesToDataset() {{
      if (rawDataset.length === 0) return;
      
      const dates = rawDataset.map(d => d.orderDate).filter(Boolean).sort();
      const minDate = dates[0] || '2023-01-01';
      const maxDate = dates[dates.length - 1] || '2024-12-31';

      document.getElementById('filterStartDate').value = minDate;
      document.getElementById('filterEndDate').value = maxDate;
      activeFilters.startDate = minDate;
      activeFilters.endDate = maxDate;

      // Populate unique categories and regions in dropdowns dynamically
      populateFilterOptions();
    }}

    function populateFilterOptions() {{
      const regions = [...new Set(rawDataset.map(r => r.region).filter(Boolean))].sort();
      const categories = [...new Set(rawDataset.map(r => r.category).filter(Boolean))].sort();
      const segments = [...new Set(rawDataset.map(r => r.segment).filter(Boolean))].sort();

      const regSelect = document.getElementById('filterRegion');
      regSelect.innerHTML = '<option value="ALL">All Regions</option>' + 
        regions.map(r => `<option value="${{r}}">${{r}}</option>`).join('');

      const catSelect = document.getElementById('filterCategory');
      catSelect.innerHTML = '<option value="ALL">All Categories</option>' + 
        categories.map(c => `<option value="${{c}}">${{c}}</option>`).join('');

      const segSelect = document.getElementById('filterSegment');
      segSelect.innerHTML = '<option value="ALL">All Segments</option>' + 
        segments.map(s => `<option value="${{s}}">${{s}}</option>`).join('');
    }}

    /* ==========================================================================
       FILTERING PIPELINE & REAL-TIME CALCULATIONS
       ========================================================================== */
    function applyFilters() {{
      const start = activeFilters.startDate;
      const end = activeFilters.endDate;
      const reg = activeFilters.region;
      const cat = activeFilters.category;
      const seg = activeFilters.segment;
      const prof = activeFilters.profitability;
      const q = activeFilters.searchQuery.toLowerCase();

      filteredData = rawDataset.filter(row => {{
        if (start && row.orderDate < start) return false;
        if (end && row.orderDate > end) return false;
        if (reg !== 'ALL' && row.region !== reg) return false;
        if (cat !== 'ALL' && row.category !== cat) return false;
        if (seg !== 'ALL' && row.segment !== seg) return false;
        if (prof === 'PROFIT' && row.profit <= 0) return false;
        if (prof === 'LOSS' && row.profit >= 0) return false;
        if (q) {{
          const match = row.productName.toLowerCase().includes(q) ||
                        row.customerName.toLowerCase().includes(q) ||
                        row.orderId.toLowerCase().includes(q) ||
                        row.state.toLowerCase().includes(q) ||
                        row.city.toLowerCase().includes(q) ||
                        row.subCategory.toLowerCase().includes(q);
          if (!match) return false;
        }}
        return true;
      }});

      // Update Filter Status Badge
      const pct = rawDataset.length > 0 ? ((filteredData.length / rawDataset.length) * 100).toFixed(1) : 0;
      document.getElementById('filteredCountBadge').textContent = 
        `Showing ${{filteredData.length.toLocaleString()}} / ${{rawDataset.length.toLocaleString()}} rows (${{pct}}%)`;

      // Update all views
      updateKPICards();
      updateInsights();
      updateCharts();
      renderTable();
    }}

    /* ==========================================================================
       1. KPI CARDS UPDATE ENGINE
       ========================================================================== */
    function updateKPICards() {{
      const totalSales = filteredData.reduce((acc, r) => acc + r.sales, 0);
      const totalProfit = filteredData.reduce((acc, r) => acc + r.profit, 0);
      const totalUnits = filteredData.reduce((acc, r) => acc + r.quantity, 0);
      const profitMargin = totalSales > 0 ? (totalProfit / totalSales) * 100 : 0;
      
      const uniqueOrders = new Set(filteredData.map(r => r.orderId)).size || (filteredData.length > 0 ? 1 : 0);
      const aov = uniqueOrders > 0 ? totalSales / uniqueOrders : 0;
      const profitPerOrder = uniqueOrders > 0 ? totalProfit / uniqueOrders : 0;

      // YoY Calculation
      // Find latest year in filtered set
      const years = [...new Set(filteredData.map(r => parseInt(r.orderDate.split('-')[0], 10)).filter(Boolean))].sort();
      let yoyPct = 0;
      let hasYoY = false;
      if (years.length >= 2) {{
        const latestYear = years[years.length - 1];
        const prevYear = latestYear - 1;
        const latestSales = filteredData.filter(r => r.orderDate.startsWith(String(latestYear))).reduce((acc, r) => acc + r.sales, 0);
        const prevSales = filteredData.filter(r => r.orderDate.startsWith(String(prevYear))).reduce((acc, r) => acc + r.sales, 0);
        if (prevSales > 0) {{
          yoyPct = ((latestSales - prevSales) / prevSales) * 100;
          hasYoY = true;
        }}
      }}

      // Format & Set Elements
      document.getElementById('kpiSales').textContent = formatCurrency(totalSales);
      document.getElementById('kpiSalesYoY').textContent = (yoyPct >= 0 ? '+' : '') + yoyPct.toFixed(1) + '% YoY';
      document.getElementById('kpiSalesYoY').className = 'kpi-trend-badge ' + (yoyPct >= 0 ? 'trend-up' : 'trend-down');

      document.getElementById('kpiProfit').textContent = formatCurrency(totalProfit);
      const profitEl = document.getElementById('kpiProfit');
      if (totalProfit >= 0) {{
        profitEl.style.color = 'var(--accent-emerald)';
        document.getElementById('kpiProfitStatus').textContent = 'Profitable';
        document.getElementById('kpiProfitStatus').className = 'kpi-trend-badge trend-up';
      }} else {{
        profitEl.style.color = 'var(--accent-rose)';
        document.getElementById('kpiProfitStatus').textContent = 'Net Loss';
        document.getElementById('kpiProfitStatus').className = 'kpi-trend-badge trend-down';
      }}

      document.getElementById('kpiMargin').textContent = profitMargin.toFixed(1) + '%';
      const marginHealth = document.getElementById('kpiMarginHealth');
      if (profitMargin >= 12) {{
        marginHealth.textContent = 'Healthy (≥12%)';
        marginHealth.className = 'kpi-trend-badge trend-up';
      }} else if (profitMargin >= 5) {{
        marginHealth.textContent = 'Moderate (5-12%)';
        marginHealth.className = 'kpi-trend-badge trend-neutral';
      }} else {{
        marginHealth.textContent = 'Low Margin (<5%)';
        marginHealth.className = 'kpi-trend-badge trend-down';
      }}

      document.getElementById('kpiOrders').textContent = uniqueOrders.toLocaleString();
      document.getElementById('kpiLineItems').textContent = `${{filteredData.length.toLocaleString()}} line items`;
      const avgItems = uniqueOrders > 0 ? (totalUnits / uniqueOrders).toFixed(1) : '0';
      document.getElementById('kpiAvgItems').textContent = `${{avgItems}} items/ord`;

      document.getElementById('kpiAOV').textContent = formatCurrency(aov);
      document.getElementById('kpiProfitPerOrder').textContent = `${{formatCurrency(profitPerOrder)}} profit/ord`;

      document.getElementById('kpiYoY').textContent = (hasYoY ? (yoyPct >= 0 ? '+' : '') + yoyPct.toFixed(1) + '%' : 'N/A');
      document.getElementById('kpiYoYBenchmark').textContent = hasYoY ? (yoyPct >= 0 ? 'Expanding' : 'Contracting') : 'Multi-year needed';
    }}

    /* ==========================================================================
       2. 4 AUTO-GENERATED STRATEGIC INSIGHTS ENGINE
       ========================================================================== */
    function updateInsights() {{
      if (filteredData.length === 0) {{
        document.getElementById('insight1Body').textContent = 'No records match active filters.';
        document.getElementById('insight2Body').textContent = 'No records match active filters.';
        document.getElementById('insight3Body').textContent = 'No records match active filters.';
        document.getElementById('insight4Body').textContent = 'No records match active filters.';
        return;
      }}

      // --- INSIGHT 1: Profitability Leakage & Sub-Category Analysis ---
      const subCatStats = {{}};
      filteredData.forEach(r => {{
        if (!subCatStats[r.subCategory]) {{
          subCatStats[r.subCategory] = {{ sales: 0, profit: 0, count: 0, totalDiscount: 0 }};
        }}
        subCatStats[r.subCategory].sales += r.sales;
        subCatStats[r.subCategory].profit += r.profit;
        subCatStats[r.subCategory].count += 1;
        subCatStats[r.subCategory].totalDiscount += r.discount;
      }});

      const subCats = Object.entries(subCatStats).map(([name, s]) => ({{
        name,
        sales: s.sales,
        profit: s.profit,
        margin: s.sales > 0 ? (s.profit / s.sales) * 100 : 0,
        avgDiscount: (s.totalDiscount / s.count) * 100,
        count: s.count
      }}));

      // Find worst profit or lowest margin subcategory
      subCats.sort((a, b) => a.profit - b.profit);
      const worstSubCat = subCats[0];
      const bestSubCat = subCats[subCats.length - 1];

      if (worstSubCat && worstSubCat.profit < 0) {{
        document.getElementById('insight1Title').textContent = `Loss Alert: ${{worstSubCat.name}} (-${{formatCurrency(Math.abs(worstSubCat.profit))}})`;
        document.getElementById('insight1Body').innerHTML = 
          `<span class="insight-metric-highlight">${{worstSubCat.name}}</span> generated <strong>${{formatCurrency(worstSubCat.sales)}}</strong> in revenue but lost <span class="insight-metric-highlight" style="color: var(--accent-rose);">${{formatCurrency(worstSubCat.profit)}}</span> (${{worstSubCat.margin.toFixed(1)}}% margin) across ${{worstSubCat.count}} orders, driven by an average discount of <strong>${{worstSubCat.avgDiscount.toFixed(1)}}%</strong>.`;
        document.getElementById('insight1Action').innerHTML = 
          `<i data-lucide="shield-alert" style="width: 14px; height: 14px;"></i><span>Action: Cap ${{worstSubCat.name}} discounts below 15% to stop leakage</span>`;
      }} else if (worstSubCat) {{
        document.getElementById('insight1Title').textContent = `Top Margin Performer: ${{bestSubCat.name}}`;
        document.getElementById('insight1Body').innerHTML = 
          `<span class="insight-metric-highlight">${{bestSubCat.name}}</span> leads profitability with <span class="insight-metric-highlight" style="color: var(--accent-emerald);">${{formatCurrency(bestSubCat.profit)}}</span> profit (${{bestSubCat.margin.toFixed(1)}}% margin), while ${{worstSubCat.name}} has the narrowest margin at ${{worstSubCat.margin.toFixed(1)}}%.`;
        document.getElementById('insight1Action').innerHTML = 
          `<i data-lucide="trending-up" style="width: 14px; height: 14px;"></i><span>Action: Scale marketing on ${{bestSubCat.name}} product lines</span>`;
      }}

      // --- INSIGHT 2: Discount Tipping Point & Margin Cliff ---
      const tiers = {{
        'zero': {{ name: '0% Discount', sales: 0, profit: 0, count: 0 }},
        'low': {{ name: '1-10% Discount', sales: 0, profit: 0, count: 0 }},
        'mid': {{ name: '11-20% Discount', sales: 0, profit: 0, count: 0 }},
        'high': {{ name: '21-40% Discount', sales: 0, profit: 0, count: 0 }},
        'extreme': {{ name: '>40% Discount', sales: 0, profit: 0, count: 0 }}
      }};

      filteredData.forEach(r => {{
        let t = 'zero';
        if (r.discount === 0) t = 'zero';
        else if (r.discount <= 0.10) t = 'low';
        else if (r.discount <= 0.20) t = 'mid';
        else if (r.discount <= 0.40) t = 'high';
        else t = 'extreme';

        tiers[t].sales += r.sales;
        tiers[t].profit += r.profit;
        tiers[t].count += 1;
      }});

      const zeroMargin = tiers.zero.sales > 0 ? (tiers.zero.profit / tiers.zero.sales) * 100 : 0;
      const midMargin = tiers.mid.sales > 0 ? (tiers.mid.profit / tiers.mid.sales) * 100 : 0;
      const highMargin = tiers.high.sales > 0 ? (tiers.high.profit / tiers.high.sales) * 100 : 0;
      const extremeMargin = tiers.extreme.sales > 0 ? (tiers.extreme.profit / tiers.extreme.sales) * 100 : 0;

      document.getElementById('insight2Title').textContent = 'Discount Cliff at 20%+ Discount';
      document.getElementById('insight2Body').innerHTML = 
        `Orders with <strong>0% discount</strong> yield <span class="insight-metric-highlight" style="color: var(--accent-emerald);">${{zeroMargin.toFixed(1)}}% margin</span>, but margins crash to <span class="insight-metric-highlight" style="color: var(--accent-rose);">${{highMargin.toFixed(1)}}%</span> at 21-40% discount and <span class="insight-metric-highlight" style="color: var(--accent-rose);">${{extremeMargin.toFixed(1)}}%</span> above 40% across ${{tiers.high.count + tiers.extreme.count}} transactions.`;
      document.getElementById('insight2Action').innerHTML = 
        `<i data-lucide="check-circle" style="width: 14px; height: 14px;"></i><span>Sweet Spot: Strict approval required for discounts exceeding 20%</span>`;

      // --- INSIGHT 3: Regional Revenue & Margin Distribution ---
      const regionStats = {{}};
      filteredData.forEach(r => {{
        if (!regionStats[r.region]) regionStats[r.region] = {{ sales: 0, profit: 0 }};
        regionStats[r.region].sales += r.sales;
        regionStats[r.region].profit += r.profit;
      }});

      const totalRev = filteredData.reduce((acc, r) => acc + r.sales, 0);
      const regionList = Object.entries(regionStats).map(([reg, s]) => ({{
        region: reg,
        sales: s.sales,
        profit: s.profit,
        share: totalRev > 0 ? (s.sales / totalRev) * 100 : 0,
        margin: s.sales > 0 ? (s.profit / s.sales) * 100 : 0
      }})).sort((a, b) => b.sales - a.sales);

      if (regionList.length > 0) {{
        const topReg = regionList[0];
        const lowMarginReg = [...regionList].sort((a, b) => a.margin - b.margin)[0];

        document.getElementById('insight3Title').textContent = `${{topReg.region}} Region Dominance (${{topReg.share.toFixed(1)}}% Sales)`;
        document.getElementById('insight3Body').innerHTML = 
          `<span class="insight-metric-highlight">${{topReg.region}}</span> leads with <strong>${{formatCurrency(topReg.sales)}}</strong> in sales (${{topReg.margin.toFixed(1)}}% margin). Conversely, <span class="insight-metric-highlight">${{lowMarginReg.region}}</span> has the lowest profit margin at <span class="insight-metric-highlight">${{lowMarginReg.margin.toFixed(1)}}%</span>.`;
        document.getElementById('insight3Action').innerHTML = 
          `<i data-lucide="map" style="width: 14px; height: 14px;"></i><span>Strategy: Audit ${{lowMarginReg.region}} discounting practices</span>`;
      }}

      // --- INSIGHT 4: Customer Segment & Seasonal Drivers ---
      const segStats = {{}};
      const monthStats = {{}};
      filteredData.forEach(r => {{
        segStats[r.segment] = (segStats[r.segment] || 0) + r.sales;
        const monthNum = parseInt(r.orderDate.split('-')[1], 10);
        monthStats[monthNum] = (monthStats[monthNum] || 0) + r.sales;
      }});

      const segSorted = Object.entries(segStats).sort((a, b) => b[1] - a[1]);
      const topSegName = segSorted[0] ? segSorted[0][0] : 'Consumer';
      const topSegSales = segSorted[0] ? segSorted[0][1] : 0;
      const topSegShare = totalRev > 0 ? (topSegSales / totalRev) * 100 : 0;

      // Q4 sales share (Nov + Dec: months 11, 12)
      const q4Sales = (monthStats[11] || 0) + (monthStats[12] || 0);
      const q4Share = totalRev > 0 ? (q4Sales / totalRev) * 100 : 0;

      document.getElementById('insight4Title').textContent = `${{topSegName}} Segment & Q4 Surge`;
      document.getElementById('insight4Body').innerHTML = 
        `<span class="insight-metric-highlight">${{topSegName}}</span> generates <strong>${{topSegShare.toFixed(1)}}%</strong> (${{formatCurrency(topSegSales)}}) of total filtered sales. Q4 (Nov-Dec) accounts for <span class="insight-metric-highlight" style="color: var(--accent-cyan);">${{q4Share.toFixed(1)}}%</span> of annual revenue velocity.`;
      document.getElementById('insight4Action').innerHTML = 
        `<i data-lucide="zap" style="width: 14px; height: 14px;"></i><span>Action: Launch early corporate retention & consumer holiday boosts</span>`;

      // Re-render lucide icons in insights
      safeCreateIcons();
    }}

    /* ==========================================================================
       3. CHARTS INITIALIZATION & UPDATE ENGINE
       ========================================================================== */
    function getChartThemeColors() {{
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      return {{
        text: isDark ? '#94A3B8' : '#64748B',
        grid: isDark ? 'rgba(255, 255, 255, 0.06)' : 'rgba(0, 0, 0, 0.06)',
        cardBg: isDark ? '#121A2B' : '#FFFFFF'
      }};
    }}

    function updateCharts() {{
      renderMonthlyChart();
      renderSegmentChart();
      renderCategoryChart();
      renderRegionChart();
      renderDiscountChart();
      renderTopProductsChart();
    }}

    // CHART 1: Monthly Trend
    function renderMonthlyChart() {{
      const ctx = document.getElementById('monthlyTrendChart').getContext('2d');
      const theme = getChartThemeColors();

      // Aggregate by YYYY-MM
      const monthlyData = {{}};
      filteredData.forEach(r => {{
        const yyyymm = r.orderDate.substring(0, 7);
        if (!monthlyData[yyyymm]) monthlyData[yyyymm] = {{ sales: 0, profit: 0 }};
        monthlyData[yyyymm].sales += r.sales;
        monthlyData[yyyymm].profit += r.profit;
      }});

      const labels = Object.keys(monthlyData).sort();
      const salesValues = labels.map(l => Math.round(monthlyData[l].sales));
      const profitValues = labels.map(l => Math.round(monthlyData[l].profit));

      // Gradients
      const salesGradient = ctx.createLinearGradient(0, 0, 0, 300);
      salesGradient.addColorStop(0, 'rgba(6, 182, 212, 0.35)');
      salesGradient.addColorStop(1, 'rgba(6, 182, 212, 0.0)');

      const profitGradient = ctx.createLinearGradient(0, 0, 0, 300);
      profitGradient.addColorStop(0, 'rgba(16, 185, 129, 0.35)');
      profitGradient.addColorStop(1, 'rgba(16, 185, 129, 0.0)');

      const datasets = [];
      if (monthlyChartView === 'both' || monthlyChartView === 'sales') {{
        datasets.push({{
          label: 'Sales Revenue',
          data: salesValues,
          borderColor: '#06B6D4',
          backgroundColor: salesGradient,
          borderWidth: 2.5,
          tension: 0.35,
          fill: true,
          pointRadius: labels.length > 24 ? 2 : 4,
          pointHoverRadius: 6,
          pointBackgroundColor: '#06B6D4'
        }});
      }}

      if (monthlyChartView === 'both' || monthlyChartView === 'profit') {{
        datasets.push({{
          label: 'Net Profit',
          data: profitValues,
          borderColor: '#10B981',
          backgroundColor: profitGradient,
          borderWidth: 2.5,
          tension: 0.35,
          fill: true,
          pointRadius: labels.length > 24 ? 2 : 4,
          pointHoverRadius: 6,
          pointBackgroundColor: '#10B981'
        }});
      }}

      if (chartMonthly) chartMonthly.destroy();

      chartMonthly = new Chart(ctx, {{
        type: 'line',
        data: {{ labels, datasets }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          interaction: {{ mode: 'index', intersect: false }},
          plugins: {{
            legend: {{
              display: true,
              position: 'top',
              labels: {{ color: theme.text, font: {{ family: 'Plus Jakarta Sans', weight: 600, size: 12 }} }}
            }},
            tooltip: {{
              callbacks: {{
                label: function(c) {{
                  return ` ${{c.dataset.label}}: ${{formatCurrency(c.parsed.y)}}`;
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              grid: {{ color: theme.grid }},
              ticks: {{ color: theme.text, font: {{ family: 'Plus Jakarta Sans', size: 11 }} }}
            }},
            y: {{
              grid: {{ color: theme.grid }},
              ticks: {{
                color: theme.text,
                font: {{ family: 'Plus Jakarta Sans', size: 11 }},
                callback: function(v) {{ return '$' + (v >= 1000 ? (v/1000).toFixed(0) + 'k' : v); }}
              }}
            }}
          }}
        }}
      }});
    }}

    function setMonthlyView(view) {{
      monthlyChartView = view;
      document.querySelectorAll('[data-chart-view]').forEach(btn => {{
        btn.classList.toggle('active', btn.getAttribute('data-chart-view') === view);
      }});
      renderMonthlyChart();
    }}

    // CHART 2: Segment Donut
    function renderSegmentChart() {{
      const ctx = document.getElementById('segmentDonutChart').getContext('2d');
      const theme = getChartThemeColors();

      const segData = {{ 'Consumer': {{ sales: 0, profit: 0 }}, 'Corporate': {{ sales: 0, profit: 0 }}, 'Home Office': {{ sales: 0, profit: 0 }} }};
      filteredData.forEach(r => {{
        const seg = segData[r.segment] ? r.segment : 'Consumer';
        segData[seg].sales += r.sales;
        segData[seg].profit += r.profit;
      }});

      const labels = Object.keys(segData);
      const sales = labels.map(l => Math.round(segData[l].sales));
      const profits = labels.map(l => Math.round(segData[l].profit));
      const totalSales = sales.reduce((a, b) => a + b, 0);

      if (chartSegment) chartSegment.destroy();

      chartSegment = new Chart(ctx, {{
        type: 'doughnut',
        data: {{
          labels: labels,
          datasets: [{{
            data: sales,
            backgroundColor: ['#6366F1', '#06B6D4', '#F59E0B'],
            borderColor: theme.cardBg,
            borderWidth: 3,
            hoverOffset: 8
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          cutout: '65%',
          plugins: {{
            legend: {{
              position: 'bottom',
              labels: {{ color: theme.text, font: {{ family: 'Plus Jakarta Sans', weight: 600, size: 12 }}, padding: 16 }}
            }},
            tooltip: {{
              callbacks: {{
                label: function(c) {{
                  const val = c.parsed;
                  const pct = totalSales > 0 ? ((val / totalSales) * 100).toFixed(1) : 0;
                  const profit = profits[c.dataIndex];
                  const margin = val > 0 ? ((profit / val) * 100).toFixed(1) : 0;
                  return [
                    ` Sales: ${{formatCurrency(val)}} (${{pct}}%)`,
                    ` Profit: ${{formatCurrency(profit)}} (${{margin}}% margin)`
                  ];
                }}
              }}
            }}
          }}
        }}
      }});
    }}

    // CHART 3: Category / Sub-Category Bar
    function renderCategoryChart() {{
      const ctx = document.getElementById('categoryBarChart').getContext('2d');
      const theme = getChartThemeColors();

      const catStats = {{}};
      const keyField = categoryDrilldown ? 'subCategory' : 'category';

      filteredData.forEach(r => {{
        const k = r[keyField] || 'Other';
        if (!catStats[k]) catStats[k] = {{ sales: 0, profit: 0 }};
        catStats[k].sales += r.sales;
        catStats[k].profit += r.profit;
      }});

      let sorted = Object.entries(catStats).map(([name, s]) => ({{
        name,
        sales: Math.round(s.sales),
        profit: Math.round(s.profit)
      }})).sort((a, b) => b.sales - a.sales);

      if (categoryDrilldown) sorted = sorted.slice(0, 12); // top 12 sub-categories

      const labels = sorted.map(s => s.name);
      const sales = sorted.map(s => s.sales);
      const profits = sorted.map(s => s.profit);

      if (chartCategory) chartCategory.destroy();

      chartCategory = new Chart(ctx, {{
        type: 'bar',
        data: {{
          labels: labels,
          datasets: [
            {{
              label: 'Sales Revenue',
              data: sales,
              backgroundColor: 'rgba(99, 102, 241, 0.85)',
              borderRadius: 6
            }},
            {{
              label: 'Net Profit',
              data: profits,
              backgroundColor: profits.map(p => p >= 0 ? 'rgba(16, 185, 129, 0.85)' : 'rgba(244, 63, 94, 0.85)'),
              borderRadius: 6
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          indexAxis: categoryDrilldown ? 'y' : 'x',
          plugins: {{
            legend: {{
              position: 'top',
              labels: {{ color: theme.text, font: {{ family: 'Plus Jakarta Sans', weight: 600, size: 12 }} }}
            }},
            tooltip: {{
              callbacks: {{
                label: function(c) {{
                  return ` ${{c.dataset.label}}: ${{formatCurrency(c.parsed[categoryDrilldown ? 'x' : 'y'])}}`;
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              grid: {{ color: theme.grid }},
              ticks: {{
                color: theme.text,
                font: {{ family: 'Plus Jakarta Sans', size: 11 }},
                callback: categoryDrilldown ? function(v) {{ return '$' + (v >= 1000 ? (v/1000).toFixed(0) + 'k' : v); }} : undefined
              }}
            }},
            y: {{
              grid: {{ color: theme.grid }},
              ticks: {{
                color: theme.text,
                font: {{ family: 'Plus Jakarta Sans', size: 11 }},
                callback: !categoryDrilldown ? function(v) {{ return '$' + (v >= 1000 ? (v/1000).toFixed(0) + 'k' : v); }} : undefined
              }}
            }}
          }}
        }}
      }});
    }}

    function toggleCategoryDrilldown(isSub) {{
      categoryDrilldown = isSub;
      document.getElementById('btnCatViewMain').classList.toggle('active', !isSub);
      document.getElementById('btnCatViewSub').classList.toggle('active', isSub);
      renderCategoryChart();
    }}

    // CHART 4: Region Bar Chart
    function renderRegionChart() {{
      const ctx = document.getElementById('regionBarChart').getContext('2d');
      const theme = getChartThemeColors();

      const regStats = {{ 'West': {{ sales: 0, profit: 0 }}, 'East': {{ sales: 0, profit: 0 }}, 'Central': {{ sales: 0, profit: 0 }}, 'South': {{ sales: 0, profit: 0 }} }};
      filteredData.forEach(r => {{
        if (!regStats[r.region]) regStats[r.region] = {{ sales: 0, profit: 0 }};
        regStats[r.region].sales += r.sales;
        regStats[r.region].profit += r.profit;
      }});

      const labels = Object.keys(regStats);
      const sales = labels.map(l => Math.round(regStats[l].sales));
      const profits = labels.map(l => Math.round(regStats[l].profit));
      const margins = labels.map(l => regStats[l].sales > 0 ? ((regStats[l].profit / regStats[l].sales) * 100).toFixed(1) : 0);

      if (chartRegion) chartRegion.destroy();

      chartRegion = new Chart(ctx, {{
        type: 'bar',
        data: {{
          labels: labels,
          datasets: [
            {{
              label: 'Sales Revenue',
              data: sales,
              backgroundColor: 'rgba(6, 182, 212, 0.85)',
              borderRadius: 6
            }},
            {{
              label: 'Net Profit',
              data: profits,
              backgroundColor: profits.map(p => p >= 0 ? 'rgba(16, 185, 129, 0.85)' : 'rgba(244, 63, 94, 0.85)'),
              borderRadius: 6
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'top',
              labels: {{ color: theme.text, font: {{ family: 'Plus Jakarta Sans', weight: 600, size: 12 }} }}
            }},
            tooltip: {{
              callbacks: {{
                afterBody: function(items) {{
                  const idx = items[0].dataIndex;
                  return `Margin: ${{margins[idx]}}%`;
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              grid: {{ color: theme.grid }},
              ticks: {{ color: theme.text, font: {{ family: 'Plus Jakarta Sans', size: 12, weight: 600 }} }}
            }},
            y: {{
              grid: {{ color: theme.grid }},
              ticks: {{
                color: theme.text,
                font: {{ family: 'Plus Jakarta Sans', size: 11 }},
                callback: function(v) {{ return '$' + (v >= 1000 ? (v/1000).toFixed(0) + 'k' : v); }}
              }}
            }}
          }}
        }}
      }});
    }}

    // CHART 5: Discount vs Profit Danger Curve
    function renderDiscountChart() {{
      const ctx = document.getElementById('discountProfitChart').getContext('2d');
      const theme = getChartThemeColors();

      // Discount buckets: 0%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%
      const buckets = [
        {{ label: '0%', min: 0, max: 0, sales: 0, profit: 0, count: 0 }},
        {{ label: '10%', min: 0.01, max: 0.10, sales: 0, profit: 0, count: 0 }},
        {{ label: '15-20%', min: 0.11, max: 0.20, sales: 0, profit: 0, count: 0 }},
        {{ label: '30-40%', min: 0.21, max: 0.40, sales: 0, profit: 0, count: 0 }},
        {{ label: '50-60%', min: 0.41, max: 0.60, sales: 0, profit: 0, count: 0 }},
        {{ label: '70-80%', min: 0.61, max: 1.00, sales: 0, profit: 0, count: 0 }}
      ];

      filteredData.forEach(r => {{
        for (const b of buckets) {{
          if (r.discount >= b.min && r.discount <= b.max) {{
            b.sales += r.sales;
            b.profit += r.profit;
            b.count += 1;
            break;
          }}
        }}
      }});

      const labels = buckets.map(b => b.label);
      const margins = buckets.map(b => b.sales > 0 ? Math.round((b.profit / b.sales) * 1000) / 10 : 0);
      const counts = buckets.map(b => b.count);

      if (chartDiscount) chartDiscount.destroy();

      chartDiscount = new Chart(ctx, {{
        type: 'bar',
        data: {{
          labels: labels,
          datasets: [{{
            label: 'Avg Profit Margin %',
            data: margins,
            backgroundColor: margins.map(m => m >= 10 ? 'rgba(16, 185, 129, 0.85)' : (m >= 0 ? 'rgba(245, 158, 11, 0.85)' : 'rgba(244, 63, 94, 0.85)')),
            borderRadius: 6
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              display: false
            }},
            tooltip: {{
              callbacks: {{
                label: function(c) {{
                  const idx = c.dataIndex;
                  return [
                    ` Avg Margin: ${{c.parsed.y}}%`,
                    ` Orders in Tier: ${{counts[idx].toLocaleString()}}`,
                    ` Sales: ${{formatCurrency(buckets[idx].sales)}}`,
                    ` Profit: ${{formatCurrency(buckets[idx].profit)}}`
                  ];
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              grid: {{ color: theme.grid }},
              ticks: {{ color: theme.text, font: {{ family: 'Plus Jakarta Sans', size: 11 }} }}
            }},
            y: {{
              grid: {{ color: theme.grid }},
              ticks: {{
                color: theme.text,
                font: {{ family: 'Plus Jakarta Sans', size: 11 }},
                callback: function(v) {{ return v + '%'; }}
              }}
            }}
          }}
        }}
      }});
    }}

    // CHART 6: Top 10 Products Ranking
    function renderTopProductsChart() {{
      const ctx = document.getElementById('topProductsChart').getContext('2d');
      const theme = getChartThemeColors();

      const prodStats = {{}};
      filteredData.forEach(r => {{
        if (!prodStats[r.productName]) prodStats[r.productName] = {{ sales: 0, profit: 0, qty: 0 }};
        prodStats[r.productName].sales += r.sales;
        prodStats[r.productName].profit += r.profit;
        prodStats[r.productName].qty += r.quantity;
      }});

      let sorted = Object.entries(prodStats).map(([name, s]) => ({{
        name: name.length > 28 ? name.substring(0, 26) + '...' : name,
        fullName: name,
        sales: Math.round(s.sales),
        profit: Math.round(s.profit),
        qty: s.qty
      }}));

      if (productRankingMode === 'sales') {{
        sorted.sort((a, b) => b.sales - a.sales);
      }} else if (productRankingMode === 'profit') {{
        sorted.sort((a, b) => b.profit - a.profit);
      }} else {{ // loss
        sorted.sort((a, b) => a.profit - b.profit);
      }}

      sorted = sorted.slice(0, 10);

      const labels = sorted.map(s => s.name);
      const dataValues = sorted.map(s => productRankingMode === 'sales' ? s.sales : s.profit);

      if (chartTopProducts) chartTopProducts.destroy();

      chartTopProducts = new Chart(ctx, {{
        type: 'bar',
        data: {{
          labels: labels,
          datasets: [{{
            label: productRankingMode === 'sales' ? 'Sales Revenue' : 'Net Profit',
            data: dataValues,
            backgroundColor: productRankingMode === 'sales' ? 'rgba(245, 158, 11, 0.85)' : 
                             (productRankingMode === 'profit' ? 'rgba(16, 185, 129, 0.85)' : 'rgba(244, 63, 94, 0.85)'),
            borderRadius: 6
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          indexAxis: 'y',
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              callbacks: {{
                title: function(items) {{
                  return sorted[items[0].dataIndex].fullName;
                }},
                label: function(c) {{
                  const item = sorted[c.dataIndex];
                  return [
                    ` Sales: ${{formatCurrency(item.sales)}}`,
                    ` Profit: ${{formatCurrency(item.profit)}}`,
                    ` Units Sold: ${{item.qty}}`
                  ];
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              grid: {{ color: theme.grid }},
              ticks: {{
                color: theme.text,
                font: {{ family: 'Plus Jakarta Sans', size: 11 }},
                callback: function(v) {{ return '$' + (Math.abs(v) >= 1000 ? (v/1000).toFixed(0) + 'k' : v); }}
              }}
            }},
            y: {{
              grid: {{ color: theme.grid }},
              ticks: {{ color: theme.text, font: {{ family: 'Plus Jakarta Sans', size: 10 }} }}
            }}
          }}
        }}
      }});
    }}

    function setProductRankingMode(mode) {{
      productRankingMode = mode;
      document.getElementById('btnTopSales').classList.toggle('active', mode === 'sales');
      document.getElementById('btnTopProfit').classList.toggle('active', mode === 'profit');
      document.getElementById('btnTopLoss').classList.toggle('active', mode === 'loss');
      renderTopProductsChart();
    }}

    /* ==========================================================================
       4. DATA EXPLORER TABLE & PAGINATION
       ========================================================================== */
    function renderTable() {{
      const tbody = document.getElementById('tableBody');
      tbody.innerHTML = '';

      if (filteredData.length === 0) {{
        tbody.innerHTML = `<tr><td colspan="11" style="text-align: center; padding: 30px; color: var(--text-muted);">No transactions match active filters.</td></tr>`;
        document.getElementById('tablePaginationInfo').textContent = 'Showing 0 of 0 entries';
        document.getElementById('tablePageNumber').textContent = '0 / 0';
        return;
      }}

      // Sort data
      const sorted = [...filteredData].sort((a, b) => {{
        let vA = a[tableSortColumn];
        let vB = b[tableSortColumn];
        if (typeof vA === 'string') vA = vA.toLowerCase();
        if (typeof vB === 'string') vB = vB.toLowerCase();
        if (vA < vB) return tableSortAsc ? -1 : 1;
        if (vA > vB) return tableSortAsc ? 1 : -1;
        return 0;
      }});

      // Pagination slice
      const totalPages = Math.ceil(sorted.length / tablePageSize) || 1;
      if (tableCurrentPage > totalPages) tableCurrentPage = totalPages;
      if (tableCurrentPage < 1) tableCurrentPage = 1;

      const startIdx = (tableCurrentPage - 1) * tablePageSize;
      const endIdx = Math.min(startIdx + tablePageSize, sorted.length);
      const pageData = sorted.slice(startIdx, endIdx);

      pageData.forEach(row => {{
        const tr = document.createElement('tr');
        const profitClass = row.profit >= 0 ? 'badge-profit-pos' : 'badge-profit-neg';
        const discStr = (row.discount * 100).toFixed(0) + '%';

        tr.innerHTML = `
          <td class="font-mono">${{row.orderDate}}</td>
          <td class="font-mono" style="font-size: 0.78rem; color: var(--text-secondary);">${{row.orderId}}</td>
          <td><strong>${{escapeHtml(row.customerName)}}</strong></td>
          <td><span style="font-size: 0.78rem;">${{row.region}} · ${{escapeHtml(row.state)}}</span></td>
          <td><span class="badge-pill" style="background: var(--bg-input);">${{row.category}}</span></td>
          <td title="${{escapeHtml(row.productName)}}">${{escapeHtml(row.productName.length > 32 ? row.productName.substring(0, 30) + '...' : row.productName)}}</td>
          <td class="font-mono" style="text-align: right;">${{formatCurrency(row.sales)}}</td>
          <td class="font-mono" style="text-align: right;">${{row.quantity}}</td>
          <td class="font-mono" style="text-align: right;">${{discStr}}</td>
          <td class="font-mono" style="text-align: right;"><span class="badge-pill ${{profitClass}}">${{formatCurrency(row.profit)}}</span></td>
          <td class="font-mono" style="text-align: right; font-weight: 700; color: ${{row.profitMargin >= 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)'}};">${{row.profitMargin.toFixed(1)}}%</td>
        `;
        tbody.appendChild(tr);
      }});

      document.getElementById('tablePaginationInfo').textContent = 
        `Showing ${{startIdx + 1}} to ${{endIdx}} of ${{sorted.length.toLocaleString()}} entries`;
      document.getElementById('tablePageNumber').textContent = `${{tableCurrentPage}} / ${{totalPages}}`;
    }}

    function sortTable(colName) {{
      if (tableSortColumn === colName) {{
        tableSortAsc = !tableSortAsc;
      }} else {{
        tableSortColumn = colName;
        tableSortAsc = (colName === 'productName' || colName === 'customerName' || colName === 'orderId');
      }}
      renderTable();
    }}

    function safeCreateIcons() {{
      if (window.lucide && typeof window.lucide.createIcons === 'function') {{
        try {{ window.lucide.createIcons(); }} catch (e) {{ console.warn('Lucide icon error', e); }}
      }}
    }}

    /* ==========================================================================
       SAMPLE CSV GENERATOR & EXPORT
       ========================================================================== */
    function downloadSampleCsv() {{
      const headers = ["Row ID", "Order ID", "Order Date", "Ship Date", "Customer Name", "Segment", "Country", "City", "State", "Postal Code", "Region", "Category", "Sub-Category", "Product Name", "Sales", "Quantity", "Discount", "Profit"];
      
      const csvRows = [headers.map(h => `"${{h}}"`).join(',')];
      rawDataset.forEach((r, idx) => {{
        const row = [
          idx + 1,
          `"${{r.orderId}}"`,
          `"${{r.orderDate}}"`,
          `"${{r.shipDate}}"`,
          `"${{r.customerName.replace(/"/g, '""')}}"`,
          `"${{r.segment}}"`,
          `"United States"`,
          `"${{r.city.replace(/"/g, '""')}}"`,
          `"${{r.state.replace(/"/g, '""')}}"`,
          `"90001"`,
          `"${{r.region}}"`,
          `"${{r.category}}"`,
          `"${{r.subCategory}}"`,
          `"${{r.productName.replace(/"/g, '""')}}"`,
          r.sales,
          r.quantity,
          r.discount,
          r.profit
        ];
        csvRows.push(row.join(','));
      }});

      const blob = new Blob([csvRows.join('\\n')], {{ type: 'text/csv;charset=utf-8;' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'kaggle_superstore_sample_dataset.csv';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      showToast('Sample Kaggle Superstore CSV downloaded! You can now load it via the upload button.', 'success');
    }}

    function exportFilteredCsv() {{
      if (filteredData.length === 0) {{
        showToast('No records to export with active filters.', 'error');
        return;
      }}

      const headers = ["Order ID", "Order Date", "Ship Date", "Customer Name", "Segment", "Region", "State", "City", "Category", "Sub-Category", "Product Name", "Sales", "Quantity", "Discount", "Profit", "Profit Margin %"];
      const csvRows = [headers.map(h => `"${{h}}"`).join(',')];

      filteredData.forEach(r => {{
        const row = [
          `"${{r.orderId}}"`,
          `"${{r.orderDate}}"`,
          `"${{r.shipDate}}"`,
          `"${{r.customerName.replace(/"/g, '""')}}"`,
          `"${{r.segment}}"`,
          `"${{r.region}}"`,
          `"${{r.state}}"`,
          `"${{r.city}}"`,
          `"${{r.category}}"`,
          `"${{r.subCategory}}"`,
          `"${{r.productName.replace(/"/g, '""')}}"`,
          r.sales,
          r.quantity,
          r.discount,
          r.profit,
          r.profitMargin
        ];
        csvRows.push(row.join(','));
      }});

      const blob = new Blob([csvRows.join('\\n')], {{ type: 'text/csv;charset=utf-8;' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `superstore_filtered_${{new Date().toISOString().split('T')[0]}}.csv`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      showToast(`Exported ${{filteredData.length.toLocaleString()}} records to CSV!`, 'success');
    }}

    /* ==========================================================================
       UTILITY & HELPER FUNCTIONS
       ========================================================================== */
    function formatCurrency(val) {{
      if (val === null || val === undefined || isNaN(val)) return '$0';
      const absVal = Math.abs(val);
      const isNeg = val < 0;
      let formatted = '';
      if (absVal >= 1000000) {{
        formatted = '$' + (absVal / 1000000).toFixed(2) + 'M';
      }} else if (absVal >= 1000) {{
        formatted = '$' + absVal.toLocaleString('en-US', {{ minimumFractionDigits: 0, maximumFractionDigits: 0 }});
      }} else {{
        formatted = '$' + absVal.toFixed(2);
      }}
      return isNeg ? '-' + formatted : formatted;
    }}

    function escapeHtml(str) {{
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }}

    function showToast(message, type = 'info') {{
      const container = document.getElementById('toastContainer');
      const toast = document.createElement('div');
      toast.className = 'toast';
      
      let icon = 'info';
      let color = 'var(--accent-cyan)';
      if (type === 'success') {{ icon = 'check-circle'; color = 'var(--accent-emerald)'; }}
      if (type === 'error') {{ icon = 'alert-triangle'; color = 'var(--accent-rose)'; }}

      toast.innerHTML = `
        <i data-lucide="${{icon}}" style="width: 18px; height: 18px; color: ${{color}};"></i>
        <span>${{escapeHtml(message)}}</span>
      `;
      container.appendChild(toast);
      safeCreateIcons();

      setTimeout(() => {{
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px)';
        toast.style.transition = 'all 0.3s ease';
        setTimeout(() => toast.remove(), 300);
      }}, 3800);
    }}

    function triggerConfetti() {{
      if (typeof confetti === 'function') {{
        confetti({{
          particleCount: 80,
          spread: 70,
          origin: {{ y: 0.6 }}
        }});
      }}
    }}

    /* ==========================================================================
       EVENT LISTENERS & APP INITIALIZATION
       ========================================================================== */
    document.addEventListener('DOMContentLoaded', () => {{
      // Initialize Lucide Icons
      safeCreateIcons();

      // Load initial demo data
      const defaultMapping = autoMapHeaders(Object.keys(INITIAL_DEMO_DATA[0]));
      rawDataset = INITIAL_DEMO_DATA.map((row, idx) => transformRawRow(row, defaultMapping, idx));
      isLiveDataset = false;

      resetFilterDatesToDataset();
      applyFilters();

      // Theme toggle setup
      const savedTheme = localStorage.getItem('insightview_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
      updateThemeIcon(savedTheme);

      document.getElementById('themeToggleBtn').addEventListener('click', () => {{
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('insightview_theme', next);
        updateThemeIcon(next);
        updateCharts(); // re-render charts with new theme colors
      }});

      function updateThemeIcon(theme) {{
        const icon = document.getElementById('themeIcon');
        if (theme === 'dark') {{
          icon.setAttribute('data-lucide', 'sun');
        }} else {{
          icon.setAttribute('data-lucide', 'moon');
        }}
        safeCreateIcons();
      }}

      // Drag and Drop Zone
      const dropZone = document.getElementById('dropZone');
      const fileInput = document.getElementById('csvFileInput');

      document.getElementById('btnLoadCsv').addEventListener('click', () => fileInput.click());
      dropZone.addEventListener('click', () => fileInput.click());

      ['dragenter', 'dragover'].forEach(name => {{
        dropZone.addEventListener(name, (e) => {{
          e.preventDefault();
          e.stopPropagation();
          dropZone.classList.add('dragover');
        }}, false);
      }});

      ['dragleave', 'drop'].forEach(name => {{
        dropZone.addEventListener(name, (e) => {{
          e.preventDefault();
          e.stopPropagation();
          dropZone.classList.remove('dragover');
        }}, false);
      }});

      dropZone.addEventListener('drop', (e) => {{
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files.length > 0) loadCsvFile(files[0]);
      }});

      fileInput.addEventListener('change', (e) => {{
        if (e.target.files.length > 0) {{
          loadCsvFile(e.target.files[0]);
        }}
      }});

      // Sample CSV & Reset Demo
      document.getElementById('btnDownloadSample').addEventListener('click', downloadSampleCsv);
      document.getElementById('btnExportFiltered').addEventListener('click', exportFilteredCsv);
      document.getElementById('btnResetDemo').addEventListener('click', () => {{
        rawDataset = INITIAL_DEMO_DATA.map((row, idx) => transformRawRow(row, defaultMapping, idx));
        isLiveDataset = false;
        loadedFileName = '';
        updateDatasetStatus(false, 'DEMO DATA - not real (160 records)');
        document.getElementById('btnResetDemo').style.display = 'none';
        resetFilterDatesToDataset();
        applyFilters();
        showToast('Reverted to demo dataset.', 'info');
      }});

      // Filters Event Handlers
      document.getElementById('filterStartDate').addEventListener('change', (e) => {{
        activeFilters.startDate = e.target.value;
        applyFilters();
      }});
      document.getElementById('filterEndDate').addEventListener('change', (e) => {{
        activeFilters.endDate = e.target.value;
        applyFilters();
      }});
      document.getElementById('filterRegion').addEventListener('change', (e) => {{
        activeFilters.region = e.target.value;
        applyFilters();
      }});
      document.getElementById('filterCategory').addEventListener('change', (e) => {{
        activeFilters.category = e.target.value;
        applyFilters();
      }});
      document.getElementById('filterSegment').addEventListener('change', (e) => {{
        activeFilters.segment = e.target.value;
        applyFilters();
      }});
      document.getElementById('filterProfitability').addEventListener('change', (e) => {{
        activeFilters.profitability = e.target.value;
        applyFilters();
      }});

      // Preset Pills
      document.querySelectorAll('.preset-pill').forEach(pill => {{
        pill.addEventListener('click', () => {{
          document.querySelectorAll('.preset-pill').forEach(p => p.classList.remove('active'));
          pill.classList.add('active');

          const preset = pill.getAttribute('data-preset');
          const allDates = rawDataset.map(r => r.orderDate).filter(Boolean).sort();
          const minDate = allDates[0] || '2021-01-01';
          const maxDate = allDates[allDates.length - 1] || '2024-12-31';

          if (preset === 'all') {{
            document.getElementById('filterStartDate').value = minDate;
            document.getElementById('filterEndDate').value = maxDate;
            activeFilters.startDate = minDate;
            activeFilters.endDate = maxDate;
          }} else if (preset === 'q4') {{
            // Filter Nov - Dec of latest year
            const latestYear = maxDate.split('-')[0];
            document.getElementById('filterStartDate').value = `${{latestYear}}-11-01`;
            document.getElementById('filterEndDate').value = `${{latestYear}}-12-31`;
            activeFilters.startDate = `${{latestYear}}-11-01`;
            activeFilters.endDate = `${{latestYear}}-12-31`;
          }} else {{
            // Year preset: '2024', '2023', etc.
            document.getElementById('filterStartDate').value = `${{preset}}-01-01`;
            document.getElementById('filterEndDate').value = `${{preset}}-12-31`;
            activeFilters.startDate = `${{preset}}-01-01`;
            activeFilters.endDate = `${{preset}}-12-31`;
          }}

          applyFilters();
        }});
      }});

      // Reset All Filters Button
      document.getElementById('btnResetFilters').addEventListener('click', () => {{
        document.querySelectorAll('.preset-pill').forEach(p => p.classList.remove('active'));
        document.querySelector('.preset-pill[data-preset="all"]').classList.add('active');
        
        document.getElementById('filterRegion').value = 'ALL';
        document.getElementById('filterCategory').value = 'ALL';
        document.getElementById('filterSegment').value = 'ALL';
        document.getElementById('filterProfitability').value = 'ALL';
        document.getElementById('tableSearchInput').value = '';

        activeFilters.region = 'ALL';
        activeFilters.category = 'ALL';
        activeFilters.segment = 'ALL';
        activeFilters.profitability = 'ALL';
        activeFilters.searchQuery = '';

        resetFilterDatesToDataset();
        applyFilters();
        showToast('All filters have been reset.', 'info');
      }});

      // Table Search & Pagination
      document.getElementById('tableSearchInput').addEventListener('input', (e) => {{
        activeFilters.searchQuery = e.target.value.trim();
        tableCurrentPage = 1;
        applyFilters();
      }});

      document.getElementById('tablePageSize').addEventListener('change', (e) => {{
        tablePageSize = parseInt(e.target.value, 10);
        tableCurrentPage = 1;
        renderTable();
      }});

      document.getElementById('btnPrevPage').addEventListener('click', () => {{
        if (tableCurrentPage > 1) {{
          tableCurrentPage--;
          renderTable();
        }}
      }});

      document.getElementById('btnNextPage').addEventListener('click', () => {{
        const totalPages = Math.ceil(filteredData.length / tablePageSize);
        if (tableCurrentPage < totalPages) {{
          tableCurrentPage++;
          renderTable();
        }}
      }});

      // Schema Diagnostics Modal
      const modal = document.getElementById('diagnosticsModal');
      document.getElementById('btnDiagnostics').addEventListener('click', () => {{
        const modalBody = document.getElementById('modalBody');
        modalBody.innerHTML = `
          <div style="background: var(--bg-input); padding: 14px; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
            <p><strong>Dataset Status:</strong> ${{isLiveDataset ? '🟢 LIVE CSV: ' + loadedFileName : '🟡 DEMO DATA'}}</p>
            <p><strong>Total Records:</strong> ${{rawDataset.length.toLocaleString()}} rows</p>
            <p><strong>Encoding Detected:</strong> ${{detectedEncoding}}</p>
          </div>
          <h4 style="font-size: 0.9rem; font-weight: 700; margin-top: 8px;">Auto-Mapped Columns:</h4>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
            ${{Object.entries(mappedColumns).map(([k, v]) => `
              <div style="background: var(--bg-input); padding: 8px 10px; border-radius: 6px; font-size: 0.76rem;">
                <span style="color: var(--text-muted);">${{k}}:</span> <strong>${{v}}</strong>
              </div>
            `).join('')}}
          </div>
        `;
        modal.classList.add('active');
        lucide.createIcons();
      }});

      document.getElementById('btnCloseModal').addEventListener('click', () => modal.classList.remove('active'));
      modal.addEventListener('click', (e) => {{
        if (e.target === modal) modal.classList.remove('active');
      }});

    }});
  </script>
</body>
</html>
'''

with open("/Users/aditijhinjar/.gemini/antigravity-ide/scratch/insightview/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html created successfully!")
