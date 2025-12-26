/**
 * Golden Ratio Typography Scale Generator
 *
 * Generate harmonious type scales based on the golden ratio
 * for web design and UI development.
 */

// Constants
const PHI = (1 + Math.sqrt(5)) / 2; // 1.618033988749895
const COMMON_RATIOS = {
  'minor-second': 1.067,
  'major-second': 1.125,
  'minor-third': 1.2,
  'major-third': 1.25,
  'perfect-fourth': 1.333,
  'augmented-fourth': 1.414,
  'perfect-fifth': 1.5,
  'golden-ratio': PHI,
  'major-sixth': 1.667,
  'minor-seventh': 1.778,
  'major-seventh': 1.875,
  'octave': 2,
};

/**
 * Generate a type scale
 * @param {number} baseSize - Base font size in pixels
 * @param {number} ratio - Scale ratio (default: golden ratio)
 * @param {number} levels - Number of levels above and below base
 * @returns {object} Type scale object
 */
function generateTypeScale(baseSize = 16, ratio = PHI, levels = 6) {
  const scale = {};

  // Smaller sizes
  for (let i = levels; i >= 1; i--) {
    const size = baseSize / Math.pow(ratio, i);
    scale[`-${i}`] = Math.round(size * 100) / 100;
  }

  // Base size
  scale['0'] = baseSize;

  // Larger sizes
  for (let i = 1; i <= levels; i++) {
    const size = baseSize * Math.pow(ratio, i);
    scale[i.toString()] = Math.round(size * 100) / 100;
  }

  return scale;
}

/**
 * Generate CSS custom properties for type scale
 * @param {number} baseSize - Base font size
 * @param {number} ratio - Scale ratio
 * @returns {string} CSS custom properties
 */
function generateCSSVariables(baseSize = 16, ratio = PHI) {
  const scale = generateTypeScale(baseSize, ratio, 6);

  let css = ':root {\n';
  css += `  /* Type Scale - Ratio: ${ratio.toFixed(3)} */\n`;
  css += `  --type-ratio: ${ratio};\n`;
  css += `  --type-base: ${baseSize}px;\n\n`;

  const sizeNames = {
    '-3': 'xs',
    '-2': 'sm',
    '-1': 'base-sm',
    '0': 'base',
    '1': 'lg',
    '2': 'xl',
    '3': '2xl',
    '4': '3xl',
    '5': '4xl',
    '6': '5xl',
  };

  for (const [level, size] of Object.entries(scale)) {
    const name = sizeNames[level] || `level-${level}`;
    css += `  --font-size-${name}: ${size}px;\n`;
  }

  css += '}\n';
  return css;
}

/**
 * Generate Tailwind CSS config for type scale
 * @param {number} baseSize - Base font size
 * @param {number} ratio - Scale ratio
 * @returns {object} Tailwind fontSize config
 */
function generateTailwindConfig(baseSize = 16, ratio = PHI) {
  const scale = generateTypeScale(baseSize, ratio, 6);

  const config = {};
  const names = ['xs', 'sm', 'base', 'lg', 'xl', '2xl', '3xl', '4xl', '5xl', '6xl'];

  let i = 0;
  for (const size of Object.values(scale)) {
    if (i < names.length) {
      // Include line height (1.5 for body, tighter for headings)
      const lineHeight = size >= baseSize * ratio ? '1.2' : '1.5';
      config[names[i]] = [`${size}px`, { lineHeight }];
      i++;
    }
  }

  return config;
}

/**
 * Calculate optimal line height using golden ratio
 * @param {number} fontSize - Font size in pixels
 * @param {number} lineWidth - Line width in characters
 * @returns {number} Recommended line height
 */
function calculateLineHeight(fontSize, lineWidth = 65) {
  // Robert Bringhurst's formula adjusted with golden ratio
  // Line height increases with line width
  const baseLineHeight = fontSize * PHI;
  const widthAdjustment = (lineWidth - 45) / 100;

  return Math.round((baseLineHeight * (1 + widthAdjustment)) * 100) / 100;
}

/**
 * Generate spacing scale based on golden ratio
 * @param {number} baseUnit - Base spacing unit in pixels
 * @returns {object} Spacing scale
 */
function generateSpacingScale(baseUnit = 8) {
  return {
    '3xs': Math.round(baseUnit / Math.pow(PHI, 3)),
    '2xs': Math.round(baseUnit / Math.pow(PHI, 2)),
    xs: Math.round(baseUnit / PHI),
    sm: baseUnit,
    md: Math.round(baseUnit * PHI),
    lg: Math.round(baseUnit * Math.pow(PHI, 2)),
    xl: Math.round(baseUnit * Math.pow(PHI, 3)),
    '2xl': Math.round(baseUnit * Math.pow(PHI, 4)),
    '3xl': Math.round(baseUnit * Math.pow(PHI, 5)),
  };
}

/**
 * Generate complete design system tokens
 * @param {object} options - Configuration options
 * @returns {object} Design tokens
 */
function generateDesignTokens(options = {}) {
  const {
    baseFontSize = 16,
    baseSpacing = 8,
    ratio = PHI,
  } = options;

  return {
    typography: {
      fontSizes: generateTypeScale(baseFontSize, ratio, 6),
      lineHeights: {
        tight: 1.2,
        snug: 1.375,
        normal: 1.5,
        relaxed: PHI,
        loose: 2,
      },
    },
    spacing: generateSpacingScale(baseSpacing),
    ratio: {
      value: ratio,
      name: Object.entries(COMMON_RATIOS).find(([, v]) => Math.abs(v - ratio) < 0.001)?.[0] || 'custom',
    },
  };
}

/**
 * Print type scale comparison
 */
function compareScales() {
  console.log('Type Scale Comparison (base: 16px)\n');
  console.log('=' .repeat(70));

  const ratiosToCompare = [
    'minor-third',
    'major-third',
    'perfect-fourth',
    'perfect-fifth',
    'golden-ratio',
  ];

  // Header
  console.log('Level'.padEnd(8) + ratiosToCompare.map(r => r.padEnd(12)).join(''));
  console.log('-'.repeat(70));

  // Generate scales
  const scales = {};
  for (const ratioName of ratiosToCompare) {
    scales[ratioName] = generateTypeScale(16, COMMON_RATIOS[ratioName], 4);
  }

  // Print each level
  for (let level = -2; level <= 4; level++) {
    const key = level.toString();
    const row = [key.padEnd(8)];

    for (const ratioName of ratiosToCompare) {
      const size = scales[ratioName][key];
      row.push(size ? `${size}px`.padEnd(12) : ''.padEnd(12));
    }

    console.log(row.join(''));
  }
}

/**
 * Demo function
 */
function demo() {
  console.log('='.repeat(60));
  console.log('GOLDEN RATIO TYPOGRAPHY SCALE GENERATOR');
  console.log('='.repeat(60));

  console.log(`\nφ (phi) = ${PHI}`);

  console.log('\n' + '-'.repeat(40));
  console.log('Type Scale (base: 16px, ratio: φ)');
  console.log('-'.repeat(40));

  const scale = generateTypeScale(16, PHI, 5);
  for (const [level, size] of Object.entries(scale)) {
    const name = level === '0' ? 'base' : `level ${level}`;
    console.log(`  ${name.padEnd(10)}: ${size}px`);
  }

  console.log('\n' + '-'.repeat(40));
  console.log('CSS Custom Properties');
  console.log('-'.repeat(40));
  console.log(generateCSSVariables(16, PHI));

  console.log('\n' + '-'.repeat(40));
  console.log('Spacing Scale (base: 8px)');
  console.log('-'.repeat(40));

  const spacing = generateSpacingScale(8);
  for (const [name, value] of Object.entries(spacing)) {
    console.log(`  ${name.padEnd(6)}: ${value}px`);
  }

  console.log('\n' + '-'.repeat(40));
  console.log('Line Height Calculations');
  console.log('-'.repeat(40));

  for (const fontSize of [12, 14, 16, 18, 24]) {
    const lineHeight = calculateLineHeight(fontSize, 65);
    console.log(`  ${fontSize}px font → ${lineHeight}px line-height (ratio: ${(lineHeight / fontSize).toFixed(2)})`);
  }

  console.log('\n');
  compareScales();

  console.log('\n' + '-'.repeat(40));
  console.log('Tailwind Config');
  console.log('-'.repeat(40));
  console.log(JSON.stringify(generateTailwindConfig(16, PHI), null, 2));
}

// Export for Node.js
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    PHI,
    COMMON_RATIOS,
    generateTypeScale,
    generateCSSVariables,
    generateTailwindConfig,
    calculateLineHeight,
    generateSpacingScale,
    generateDesignTokens,
    compareScales,
    demo,
  };
}

// Run demo if executed directly
if (typeof require !== 'undefined' && require.main === module) {
  demo();
}
