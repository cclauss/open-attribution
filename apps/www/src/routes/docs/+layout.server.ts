export const csr = false;

import { PUBLIC_DOCS_HOST } from '$env/static/public';

async function fetchContent(url) {
	let htmlContent;
	if (url && !url.pathname.includes('.')) {
		// Ensure the path correctly points to where mkdocs HTML files are located.
		// ie www/static/documentation/docs/index.html
		const processedPathname = url.pathname.replace('/docs/', '');
		var mypath = `${PUBLIC_DOCS_HOST}/generated-docs/${processedPathname}index.html`;
		console.log(`Try rendering static path= ${mypath}`);
		const response = await fetch(mypath);
		if (response.ok) {
			htmlContent = await response.text();
		} else {
			htmlContent = 'Page not found.';
		}
	}
	// console.log(`GOT CONTENT: ${htmlContent}`)
	return htmlContent;
}

export async function load({ url }) {
	const myhtml = await fetchContent(url);
	return {
		props: {
			mydocs: myhtml
		}
	};
}
