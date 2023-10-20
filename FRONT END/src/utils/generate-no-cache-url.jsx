export const generateNocacheURL = (url_string) => {
    const randomURL = url_string + '?v=' + Date.now().toString();
    return randomURL
}