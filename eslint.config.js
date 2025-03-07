/** @type {import('eslint').Linter.Config} */
module.exports = [
  {
    languageOptions: {
      parserOptions: {
        ecmaVersion: 2020,
        sourceType: "module",
      },
    },
    rules: {
      "no-console": "warn",
    },
  },
];
