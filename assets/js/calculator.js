document.addEventListener('DOMContentLoaded', () => {
  const calcSection = document.getElementById('roi-calculator');
  if (!calcSection) return;

  const incomeInput = document.getElementById('monthly-income');
  const incomeValue = document.getElementById('income-value');
  const platformSelect = document.getElementById('platform-select');
  const yearsInput = document.getElementById('years');
  const yearsValue = document.getElementById('years-value');

  const outMonthly = document.getElementById('out-monthly');
  const outYearly = document.getElementById('out-yearly');
  const outTotal = document.getElementById('out-total');
  const outWebsite = document.getElementById('out-website');
  const outBreakeven = document.getElementById('out-breakeven');
  const outSavings = document.getElementById('out-savings');
  const outConclusion = document.getElementById('out-conclusion');

  const WEBSITE_COST = 1200; // Using mid-point of 900-1500

  const updateCalculator = () => {
    const income = parseFloat(incomeInput.value);
    const platformCutPct = parseFloat(platformSelect.value);
    const years = parseInt(yearsInput.value);

    incomeValue.innerText = `€${income.toLocaleString()}`;
    yearsValue.innerText = `${years} Year${years > 1 ? 's' : ''}`;

    const monthlyLost = income * (platformCutPct / 100);
    const yearlyLost = monthlyLost * 12;
    const totalLost = yearlyLost * years;

    const breakEvenMonths = Math.ceil(WEBSITE_COST / monthlyLost);
    const totalSavings = totalLost - WEBSITE_COST;

    outMonthly.innerText = `€${monthlyLost.toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0})}`;
    outYearly.innerText = `€${yearlyLost.toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0})}`;
    outTotal.innerText = `€${totalLost.toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0})}`;
    outWebsite.innerText = `€${WEBSITE_COST.toLocaleString()}`;
    
    if (monthlyLost > 0) {
      outBreakeven.innerText = `${breakEvenMonths} Months`;
      outSavings.innerText = `€${totalSavings.toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0})}`;
      outConclusion.innerText = `With your own website, you keep €${yearlyLost.toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0})} more per year — your site pays for itself in ${breakEvenMonths} months.`;
    } else {
      outBreakeven.innerText = `-`;
      outSavings.innerText = `-`;
      outConclusion.innerText = `Start earning on your own platform with zero commission cuts.`;
    }
  };

  incomeInput.addEventListener('input', updateCalculator);
  platformSelect.addEventListener('change', updateCalculator);
  yearsInput.addEventListener('input', updateCalculator);

  updateCalculator();
});
