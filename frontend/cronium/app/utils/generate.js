export default function generate(...classes) {
	return classes.filter(Boolean).join(" ");
}