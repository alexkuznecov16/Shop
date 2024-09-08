function changeLanguage(lang) {
	var currentUrl = window.location.href;
	var newUrl = currentUrl.replace(/\/(ru|lv)\//, '/' + lang + '/');

	if (!newUrl.match(/\/(ru|lv)\//)) {
		newUrl = currentUrl + (currentUrl.endsWith('/') ? '' : '/') + lang + '/';
	}

	window.location.href = newUrl;
}
