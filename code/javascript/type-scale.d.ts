/**
 * Type definitions for golden-ratio-toolkit
 */

/**
 * The golden ratio (phi)
 */
export const PHI: number;

/**
 * Common typographic ratios
 */
export const COMMON_RATIOS: {
  'minor-second': number;
  'major-second': number;
  'minor-third': number;
  'major-third': number;
  'perfect-fourth': number;
  'augmented-fourth': number;
  'perfect-fifth': number;
  'golden-ratio': number;
  'major-sixth': number;
  'minor-seventh': number;
  'major-seventh': number;
  'octave': number;
};

/**
 * Generate a type scale
 * @param baseSize - Base font size in pixels
 * @param ratio - Scale ratio (default: golden ratio)
 * @param levels - Number of levels above and below base
 * @returns Type scale object mapping level to size
 */
export function generateTypeScale(
  baseSize?: number,
  ratio?: number,
  levels?: number
): Record<string, number>;

/**
 * Generate CSS custom properties for type scale
 * @param baseSize - Base font size
 * @param ratio - Scale ratio
 * @returns CSS custom properties string
 */
export function generateCSSVariables(
  baseSize?: number,
  ratio?: number
): string;

/**
 * Generate Tailwind CSS config for type scale
 * @param baseSize - Base font size
 * @param ratio - Scale ratio
 * @returns Tailwind fontSize config object
 */
export function generateTailwindConfig(
  baseSize?: number,
  ratio?: number
): Record<string, [string, { lineHeight: string }]>;

/**
 * Calculate optimal line height using golden ratio
 * @param fontSize - Font size in pixels
 * @param lineWidth - Line width in characters
 * @returns Recommended line height
 */
export function calculateLineHeight(
  fontSize: number,
  lineWidth?: number
): number;

/**
 * Generate spacing scale based on golden ratio
 * @param baseUnit - Base spacing unit in pixels
 * @returns Spacing scale object
 */
export function generateSpacingScale(
  baseUnit?: number
): Record<string, number>;

/**
 * Design tokens configuration
 */
export interface DesignTokensOptions {
  baseFontSize?: number;
  baseSpacing?: number;
  ratio?: number;
}

/**
 * Design tokens output
 */
export interface DesignTokens {
  typography: {
    fontSizes: Record<string, number>;
    lineHeights: {
      tight: number;
      snug: number;
      normal: number;
      relaxed: number;
      loose: number;
    };
  };
  spacing: Record<string, number>;
  ratio: {
    value: number;
    name: string;
  };
}

/**
 * Generate complete design system tokens
 * @param options - Configuration options
 * @returns Design tokens
 */
export function generateDesignTokens(
  options?: DesignTokensOptions
): DesignTokens;

/**
 * Print type scale comparison to console
 */
export function compareScales(): void;

/**
 * Run demo
 */
export function demo(): void;
