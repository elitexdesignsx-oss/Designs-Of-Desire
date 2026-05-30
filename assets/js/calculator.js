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
  const outBreakevenLabel = document.getElementById('out-breakeven-label');
  const outSavingsLabel = document.getElementById('out-savings-label');
  const calcExplainerTitle = document.getElementById('calc-explainer-title');
  const calcExplainerText = document.getElementById('calc-explainer-text');

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
    const platformFeeNote = platformKind === 'fee'
      ? `${platformName} includes two issues in this estimate: about ${missedPct}% missed potential before people buy, then a ${feePct}% platform fee on what remains.`
      : `${platformName} has no platform fee counted here. This estimates about ${missedPct}% missed potential from weak routing, unclear offer, or no direct sales path.`;

    outMonthly.innerText = `€${monthlyLeakage.toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0})}`;
    outYearly.innerText = `€${monthlyRecovery.toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0})}`;
    if (outAfterMonthly) {
      outAfterMonthly.innerText = `€${monthlyAfterWebsite.toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0})}`;
    }
    if (outYearlySaved) {
      outYearlySaved.innerText = `€${yearlyRecovery.toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0})}`;
    }
    outWebsite.innerText = `€${websiteCost.toLocaleString()}`;
    if (outPackageName) {
      outPackageName.innerText = packageName;
    }

    if (outBreakevenLabel) {
      outBreakevenLabel.innerText = 'Estimated time to cover the website cost:';
    }
    if (outSavingsLabel) {
      outSavingsLabel.innerText = 'Net recovered value after website cost:';
    }
    if (outMonthlyHelp) {
      outMonthlyHelp.innerText = platformKind === 'fee'
        ? `About €${monthlyMissedPotential.toLocaleString(undefined, {maximumFractionDigits: 0})} missed before buying + €${monthlyPlatformFee.toLocaleString(undefined, {maximumFractionDigits: 0})} in ${platformName} fees.`
        : `Mostly missed buying-path value. No platform fee is counted for ${platformName}.`;
    }
    if (outYearlyHelp) {
      outYearlyHelp.innerText = `${packageName} uses a ${recoveryPct}% recovery estimate from the full potential.`;
    }

    if (calcExplainerTitle && calcExplainerText) {
      if (platformKind === 'fee') {
        calcExplainerTitle.innerText = `${platformName}: missed sales + platform fee`;
        calcExplainerText.innerText = `You currently keep €${income.toLocaleString()}. The calculator works backward: €${income.toLocaleString()} ÷ ${(visibilityFactor * 100).toFixed(0)}% ÷ ${(feeFactor * 100).toFixed(0)}% = about €${fullMonthlyPotential.toLocaleString(undefined, {maximumFractionDigits: 0})} full potential. The monthly leak is about €${monthlyMissedPotential.toLocaleString(undefined, {maximumFractionDigits: 0})} in missed buying-path value plus €${monthlyPlatformFee.toLocaleString(undefined, {maximumFractionDigits: 0})} in platform fees.`;
      } else {
        calcExplainerTitle.innerText = `${platformName}: attention without a clear buying path`;
        calcExplainerText.innerText = `You currently keep €${income.toLocaleString()}. ${platformName} has no platform fee counted here, so the calculator works backward from the buying-path loss: €${income.toLocaleString()} ÷ ${(visibilityFactor * 100).toFixed(0)}% = about €${fullMonthlyPotential.toLocaleString(undefined, {maximumFractionDigits: 0})} full potential. That means roughly €${monthlyLeakage.toLocaleString(undefined, {maximumFractionDigits: 0})} is leaking each month.`;
      }
    }
    
    if (monthlyRecovery > 0) {
      outBreakeven.innerText = `${breakEvenMonths} Month${breakEvenMonths === 1 ? '' : 's'}`;
      outSavings.innerText = `€${netPotential.toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0})}`;
      if (packageName === 'Full Custom Website') {
        outConclusion.innerText = `${platformFeeNote} ${packageName} aims to recover ${recoveryPct}% of full potential through premium presentation, clearer offers, routing, and booking/contact flow.`;
      } else if (packageName === 'Creator Commerce Platform') {
        outConclusion.innerText = `${platformFeeNote} ${packageName} aims to recover ${recoveryPct}% of full potential through direct payments, shop structure, subscriptions, and members access.`;
      } else {
        outConclusion.innerText = `${platformFeeNote} ${packageName} aims to recover up to ${recoveryPct}% of full potential through direct sales, automations, dashboards, chatbot flows, custom booking, and follow-ups.`;
      }
    } else {
      outBreakeven.innerText = `-`;
      outSavings.innerText = `-`;
      outConclusion.innerText = `Use this as a planning estimate once you have consistent traffic and a clear offer.`;
    }
  };

  incomeInput.addEventListener('input', updateCalculator);
  platformSelect.addEventListener('change', updateCalculator);
  websitePackageSelect.addEventListener('change', updateCalculator);
  yearsInput.addEventListener('input', updateCalculator);

  updateCalculator();
});
