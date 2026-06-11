document.addEventListener('DOMContentLoaded', () => {
  const calcSection = document.getElementById('roi-calculator');
  if (!calcSection) return;

  const incomeInput = document.getElementById('monthly-income');
  const incomeValue = document.getElementById('income-value');
  const platformSelect = document.getElementById('platform-select');
  const websitePackageSelect = document.getElementById('website-package');
  const yearsInput = document.getElementById('years');
  const yearsValue = document.getElementById('years-value');

  const outMonthly = document.getElementById('out-monthly');
  const outYearly = document.getElementById('out-yearly');
  const outAfterMonthly = document.getElementById('out-after-monthly');
  const outYearlySaved = document.getElementById('out-yearly-saved');
  const outWebsite = document.getElementById('out-website');
  const outPackageName = document.getElementById('out-package-name');
  const outBreakeven = document.getElementById('out-breakeven');
  const outSavings = document.getElementById('out-savings');
  const outConclusion = document.getElementById('out-conclusion');
  const outMonthlyHelp = document.getElementById('out-monthly-help');
  const outYearlyHelp = document.getElementById('out-yearly-help');
  const outSavingsLabel = document.getElementById('out-savings-label');
  const calcExplainerTitle = document.getElementById('calc-explainer-title');
  const outPlatformName = document.getElementById('out-platform-name');

  const formatCurrency = (value) => `€${value.toLocaleString(undefined, {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  })}`;

  const updateCalculator = () => {
    const income = parseFloat(incomeInput.value);
    const selectedPlatform = platformSelect.options[platformSelect.selectedIndex];
    const platformName = selectedPlatform.value;
    const platformKind = selectedPlatform.dataset.kind;
    const missedPct = parseFloat(selectedPlatform.dataset.missed);
    const feePct = parseFloat(selectedPlatform.dataset.fee);
    const websiteCost = parseFloat(websitePackageSelect.value);
    const selectedPackage = websitePackageSelect.options[websitePackageSelect.selectedIndex];
    const packageName = selectedPackage.dataset.name;
    const recoveryPct = parseFloat(selectedPackage.dataset.potential);
    const years = parseInt(yearsInput.value);

    incomeValue.innerText = `€${income.toLocaleString()}`;
    yearsValue.innerText = `${years} Year${years > 1 ? 's' : ''}`;

    const visibilityFactor = 1 - (missedPct / 100);
    const feeFactor = 1 - (feePct / 100);
    const fullMonthlyPotential = income / (visibilityFactor * feeFactor);
    const monthlyMissedPotential = fullMonthlyPotential * (missedPct / 100);
    const monthlyPlatformFee = (fullMonthlyPotential - monthlyMissedPotential) * (feePct / 100);
    const monthlyLeakage = fullMonthlyPotential - income;
    const monthlyRecovery = fullMonthlyPotential * (recoveryPct / 100);
    const monthlyAfterWebsite = income + monthlyRecovery;
    const yearlyRecovery = monthlyRecovery * 12;
    const totalRecovery = yearlyRecovery * years;

    const breakEvenMonths = monthlyRecovery > 0 ? Math.ceil(websiteCost / monthlyRecovery) : 0;
    const netPotential = totalRecovery - websiteCost;
    const timeframeLabel = `${years} year${years > 1 ? 's' : ''}`;

    outMonthly.innerText = formatCurrency(monthlyLeakage);
    outYearly.innerText = `${formatCurrency(monthlyRecovery)}/month`;
    if (outAfterMonthly) {
      outAfterMonthly.innerText = formatCurrency(monthlyAfterWebsite);
    }
    if (outYearlySaved) {
      outYearlySaved.innerText = formatCurrency(totalRecovery);
    }
    outWebsite.innerText = formatCurrency(websiteCost);
    if (outPackageName) {
      outPackageName.innerText = packageName;
    }
    if (outPlatformName) {
      outPlatformName.innerText = platformName;
    }

    if (outSavingsLabel) {
      outSavingsLabel.innerText = 'Net recovered value after website cost:';
    }
    if (outMonthlyHelp) {
      outMonthlyHelp.innerText = platformKind === 'fee'
        ? `Includes about ${formatCurrency(monthlyMissedPotential)} missed before buying plus ${formatCurrency(monthlyPlatformFee)} in ${platformName} fees.`
        : `Estimated from weak routing, unclear offer, or no direct sales path. No platform fee is counted for ${platformName}.`;
    }
    if (outYearlyHelp) {
      outYearlyHelp.innerText = `${packageName} uses a ${recoveryPct}% recovery estimate from the full potential.`;
    }

    if (calcExplainerTitle) {
      calcExplainerTitle.innerText = `${platformName}: calculation note`;
    }
    
    if (monthlyRecovery > 0) {
      outBreakeven.innerText = `${breakEvenMonths} Month${breakEvenMonths === 1 ? '' : 's'}`;
      outSavings.innerText = formatCurrency(netPotential);
      if (outConclusion) {
        outConclusion.innerText = `Over ${timeframeLabel}, that is roughly ${formatCurrency(totalRecovery)} in recovered potential for a one-time ${formatCurrency(websiteCost)} investment.`;
      }
    } else {
      outBreakeven.innerText = `-`;
      outSavings.innerText = `-`;
      if (outConclusion) {
        outConclusion.innerText = `Use this as a planning estimate once you have consistent traffic and a clear offer.`;
      }
    }
  };

  incomeInput.addEventListener('input', updateCalculator);
  platformSelect.addEventListener('change', updateCalculator);
  websitePackageSelect.addEventListener('change', updateCalculator);
  yearsInput.addEventListener('input', updateCalculator);

  updateCalculator();
});
