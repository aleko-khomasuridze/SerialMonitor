function themeChanger() {
    const htmlElement = document.documentElement;

    // Toggle the attribute value and local storage setting for theme.
    if (htmlElement.getAttribute('data-bs-theme') === 'dark') {
        htmlElement.setAttribute('data-bs-theme', 'light');
        localStorage.setItem('theme', 'light'); 
    } else {
        htmlElement.setAttribute('data-bs-theme', 'dark');
        localStorage.setItem('theme', 'dark'); 
    }
}