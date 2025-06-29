import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import "package:aqi_app/constants/urls.dart" as urls;

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final emailRegex = RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$');

  Future<void> _submitForm({required email, required password}) async {
    final apiUri = Uri.parse(urls.kLOGIN_MANUAL_URL);
    try {
      final response = await http.post(
        apiUri,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({"email": email, "password": password}),
      );
      if (response.statusCode == 200 || response.statusCode == 201) {
        // Success response
        final tokens = jsonDecode(response.body);
        final accessToken = tokens["access_token"];
        final refreshToken = tokens["refresh_token"];
        SharedPreferences prefs = await SharedPreferences.getInstance();
        await prefs.setString("accessToken", accessToken);
        await prefs.setString("refreshToken", refreshToken);

      } else {
        // Some error
        final error = jsonDecode(response.body);
        print(error);
      }
    } catch (e) {
      print("Error: ${e}");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Login Page"), backgroundColor: Colors.red),
      body: Center(
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                controller: _emailController,
                decoration: InputDecoration(labelText: "Email"),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter the email';
                  }
                  if (!emailRegex.hasMatch(value)) {
                    return 'Please enter a valid email address';
                  }
                },
              ),
              TextFormField(
                controller: _passwordController,
                obscureText: true,
                decoration: InputDecoration(labelText: "Password"),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter the password';
                  }
                  return null;
                },
              ),
              MaterialButton(
                onPressed: () async {
                  if (_formKey.currentState!.validate()) {
                    await _submitForm(
                      email: _emailController.text,
                      password: _passwordController.text,
                    );
                  }
                },
                child: Text("Login"),
              ),
              SizedBox(height: 30),
              ElevatedButton(
                onPressed: () {},
                child: Text("Login with Google"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
