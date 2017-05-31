extern crate gio;
extern crate gtk;
extern crate webkit2gtk;
extern crate html5ever;

use std::env;

use gtk::prelude::*;
use gtk::{Application, ApplicationWindow, Label};

fn main() {
    if gtk::init().is_err() {
        println!("Failed to initialize GTK!");
        return;
    }

    let app = Application::new(Some("bit.espectalll.Scribe"), gio::APPLICATION_FLAGS_NONE).unwrap();

    app.connect_activate(move |app| {
        /*
        let main_window = ApplicationWindow::new(&app);
        main_window.set_title("Scribe");
        main_window.set_default_size(350, 70);
        let label = Label::new("Hey, listen!");
        main_window.add(&label);
        */
        let builder =

        main_window.connect_delete_event(|_, _| {
            gtk::main_quit();
            Inhibit(false)
        });

        app.add_window(&main_window);
        main_window.set_application(Some(app));
        main_window.show_all();
    });


    let args = env::args().collect::<Vec<_>>();
    let args_refs = args.iter().map(|x| &x[..]).collect::<Vec<_>>();

    app.run(args_refs.len() as i32, &args_refs);
}
